#!/usr/bin/env python
from pathlib import Path

from bokeh.io import output_file, save
from bokeh.models import HoverTool, ResetTool, WheelZoomTool
from bokeh.models.formatters import DatetimeTickFormatter
from bokeh.palettes import Blues4
from bokeh.plotting import figure, reset_output
import pandas as pd


ROOT_DIR = Path(__file__).parent.parent

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

for pkg in pkg_dfs:
    df = pkg_dfs[pkg]
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


metrics_md = """# Metrics

Below are some of the metrics of things that Xdev does.

## Package Downloads
"""

for pkg in pkg_dfs:
    metrics_md += f"""
### {pkg}

:::{{raw}} html
---
file: ../images/metrics/{pkg}-downloads.html
---
:::

"""

with open(ROOT_DIR / 'status/metrics.md', 'w') as f:
    f.write(metrics_md)
