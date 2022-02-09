#!/usr/bin/env python
from datetime import datetime
from math import pi
from pathlib import Path

from bokeh.io import output_file, save
from bokeh.models import HoverTool, ResetTool, WheelZoomTool
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.palettes import Blues4
from bokeh.plotting import figure, reset_output
from bokeh.transform import cumsum
from dateutil.relativedelta import relativedelta
import numpy as np
import pandas as pd

ROOT_DIR = Path(__file__).parent.parent
XDEV_AUTHORS = set(['andersy005', 'kmpaul', 'jukent', 'matt-long', 'mgrover1'])


def get_downloads_data() -> pd.DataFrame:
    df_pypi = pd.read_csv('data/pypi_stats.csv', index_col='month')
    df_pypi.index = pd.to_datetime(df_pypi.index)

    df_conda = pd.read_csv('data/conda_stats.csv', index_col='month')
    df_conda.index = pd.to_datetime(df_conda.index)

    pkgs = set(df_pypi.columns).union(df_conda.columns)
    pkg_dfs = {}
    for pkg in pkgs:
        df = pd.DataFrame()
        df.index = pd.period_range(
            start='2019-01',
            periods=0,
            freq='M',
            name='month',
        )
        include_df = False
        if pkg in df_pypi and df_pypi[pkg].sum() > 0:
            df['PyPI'] = df_pypi[pkg]
            df['PyPI'] = df['PyPI'].fillna(0).astype('int64')
            include_df = True
        if pkg in df_conda and df_conda[pkg].sum() > 0:
            df['Conda'] = df_conda[pkg]
            df['Conda'] = df['Conda'].fillna(0).astype('int64')
            include_df = True
        if include_df:
            pkg_dfs[pkg] = df

    return pkg_dfs


def make_downloads_images(dl_dfs: pd.DataFrame):
    for pkg in dl_dfs:
        df = dl_dfs[pkg]
        names = list(df.columns)
        if len(names) == 0:
            continue

        reset_output()
        output_file(ROOT_DIR / f'images/metrics/{pkg}-downloads.html')

        dtformatter = DatetimeTickFormatter(
            days='%d %b %Y',
            months='%b %Y',
        )

        tools = [
            WheelZoomTool(dimensions='width'),
            HoverTool(
                tooltips=[
                    ('Source', '$name'),
                    ('Downloads', '@$name'),
                    ('Date', '@month{%b %Y}'),
                ],
                formatters={
                    '@month': 'datetime',
                },
            ),
            ResetTool(),
        ]

        p = figure(
            title='Package Downloads',
            height=300,
            width=800,
            toolbar_location='right',
            tools=tools,
            x_range=(df.index.min(), df.index.max()),
            y_range=(0, df.sum(axis=1).max()*1.1),
            sizing_mode='scale_width',
        )
        p.varea_stack(
            stackers=names,
            x='month',
            color=Blues4[:len(names)],
            legend_label=names,
            source=df,
        )
        p.vline_stack(
            stackers=names,
            x='month',
            color=Blues4[:len(names)],
            source=df,
        )
        p.xaxis.formatter = dtformatter
        p.legend.location = 'top_left'
        save(p)


def get_repo_data() -> pd.DataFrame:
    df = pd.read_csv('data/github_repos.csv')
    df.package = df.package.apply(lambda x: x.replace('_', '-'))
    return df


def get_commits_data() -> pd.DataFrame:
    return pd.read_csv('data/github_commits.csv')


def make_commit_images(co_df: pd.DataFrame):
    def contrib_type(author):
        if author in XDEV_AUTHORS:
            return 'Internal'
        elif '[bot]' in str(author):
            return 'Bot'
        else:
            return 'External'
    co_df['Contributor'] = co_df.author.apply(contrib_type)
    co_df['changes'] = co_df.additions + co_df.deletions

    co_df = co_df.loc[co_df['Contributor'] != 'Bot']
    co_df = co_df.groupby(by=['package', 'Contributor']).sum().changes.reset_index()

    for pkg in co_df.package.unique():
        df = co_df.loc[co_df.package == pkg][['Contributor', 'changes']]
        df = df.sort_values('Contributor', ascending=False).reset_index(drop=True)
        df['frac'] = df['changes'] / df['changes'].sum()
        df['pct'] = df['frac'].apply(lambda x: f'{x * 100:0.1f}%')
        df['angle'] = df['frac'] * 2 * pi
        df['color'] = Blues4[:len(df)]

        reset_output()
        output_file(ROOT_DIR / f'images/metrics/{pkg}-commits.html')

        p = figure(
            title='Commit Contributions',
            height=250,
            width=250,
            toolbar_location='right',
            tools='hover',
            tooltips='@Contributor: @pct',
            x_range=(-1, 1),
            y_range=(-1, 1),
        )
        if len(df) == 1:
            p.circle(x=0, y=0, radius=0.975, line_color='white', fill_color='color', source=df)
        else:
            p.wedge(x=0, y=0, radius=0.975,
                    start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                    line_color='white', fill_color='color', source=df)
        p.axis.axis_label = None
        p.axis.visible = False
        p.grid.grid_line_color = None
        p.outline_line_color = None
        save(p)


def make_contributor_images(co_df: pd.DataFrame):
    def is_not_bot(author):
        return '[bot]' not in str(author)

    df_contributors = pd.DataFrame()
    df_contributors['Total'] = co_df.groupby(by='package').author.unique().apply(
        lambda x: np.vectorize(is_not_bot)(x).sum()
    )
    df_contributors['Internal'] = co_df.groupby(by='package').author.unique().apply(
        lambda x: np.isin(x, tuple(XDEV_AUTHORS)).sum()
    )
    df_contributors['External'] = df_contributors['Total'] - df_contributors['Internal']
    df_contributors = df_contributors.drop(columns=['Total'])
    df_contributors = df_contributors.transpose()

    for pkg in df_contributors:
        df = df_contributors[pkg].to_frame(name='number')
        df['angle'] = df / df.sum() * 2 * pi
        df['color'] = Blues4[:2]

        reset_output()
        output_file(ROOT_DIR / f'images/metrics/{pkg}-contributors.html')

        p = figure(
            title='Unique Contributors',
            height=250,
            width=250,
            toolbar_location='right',
            tools='hover',
            tooltips='@index: @number',
            x_range=(-1, 1),
            y_range=(-1, 1),
        )
        if df['number'].loc['External'] == 0:
            df = df.drop(index='External')
            p.circle(x=0, y=0, radius=0.975, line_color='white', fill_color='color', source=df)
        else:
            p.wedge(x=0, y=0, radius=0.975,
                    start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
                    line_color='white', fill_color='color', source=df)
        p.axis.axis_label = None
        p.axis.visible = False
        p.grid.grid_line_color = None
        p.outline_line_color = None
        save(p)


def get_issue_data() -> pd.DataFrame:
    df = pd.read_csv('data/github_issues.csv')
    df.created = pd.to_datetime(df.created).dt.tz_localize(None)
    df.closed = pd.to_datetime(df.closed).dt.tz_localize(None)
    df['is_open'] = df.closed.apply(lambda x: pd.isnull(x))
    return df


def make_burndown_images(iss_df: pd.DataFrame):
    for pkg in iss_df.package.unique():
        df = pd.DataFrame(columns=['nopen'])
        df_pkg_issues = iss_df.loc[iss_df.package == pkg]
        start_time = df_pkg_issues.created.min() - relativedelta(months=1)
        end_time = datetime.today()
        for month in pd.date_range(start=start_time, end=end_time, freq='M'):
            _df = df_pkg_issues.loc[
                (df_pkg_issues.created <= month) & (df_pkg_issues.package == pkg)
            ]
            _df = _df.loc[(_df.is_open) | (_df.closed > month)]
            df.loc[month] = _df.number.count()

        reset_output()
        output_file(ROOT_DIR / f'images/metrics/{pkg}-burndown.html')

        dtformatter = DatetimeTickFormatter(
            days='%d %b %Y',
            months='%b %Y',
        )

        p = figure(
            title='Open Issues',
            height=300,
            width=800,
            toolbar_location='right',
            tools=[
                HoverTool(
                    tooltips=[
                        ('Issues', '@nopen'),
                        ('Date', '@index{%b %Y}'),
                    ],
                    formatters={
                        '@index': 'datetime',
                    },
                )
            ],
            x_range=(df.index.min(), df.index.max()),
            y_range=(0, df.nopen.max()*1.1),
            sizing_mode='scale_width',
        )
        p.varea(x='index', y1=0, y2='nopen', fill_color=Blues4[0], source=df)
        p.line(x='index', y='nopen', line_color=Blues4[0], source=df)
        p.xaxis.formatter = dtformatter
        save(p)


def make_metrics_markdown(packages):
    metrics_md = """# Metrics

Below are some of the metrics of things that Xdev does.

## Package Downloads
"""

    for pkg in packages:
        metrics_md += f"""
### {pkg}

:::{{raw}} html
---
file: ../images/metrics/{pkg}-downloads.html
---
:::

:::{{raw}} html
---
file: ../images/metrics/{pkg}-commits.html
---
:::

:::{{raw}} html
---
file: ../images/metrics/{pkg}-contributors.html
---
:::

:::{{raw}} html
---
file: ../images/metrics/{pkg}-burndown.html
---
:::

"""

    with open(ROOT_DIR / 'status/metrics.md', 'w') as f:
        f.write(metrics_md)


if __name__ == '__main__':
    dl_dfs = get_downloads_data()
    make_downloads_images(dl_dfs)

    co_df = get_commits_data()
    make_commit_images(co_df)
    make_contributor_images(co_df)

    iss_df = get_issue_data()
    make_burndown_images(iss_df)

    repos = get_repo_data()
    packages = repos.package.to_list()
    make_metrics_markdown(packages)
