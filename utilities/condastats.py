#!/usr/bin/env python
from datetime import datetime
from dateutil.relativedelta import relativedelta
from pathlib import Path

import dask.dataframe as dd
import pandas as pd

from common import update_stats, read_stats_file
from xdevrepos import read_repos_file, get_packages


STATS_FILE = Path(__file__).with_suffix('.csv')


def get_conda_stats(packages=[], year=None, month=None):
    """
    Read Conda download statistics from AWS S3

    This function readS data from a public AWS S3 store containing hourly
    Conda package download data.
    """
    if not packages:
        return None

    if isinstance(year, (list, tuple)):
        years = [f'{y:04d}' for y in year]
    elif isinstance(year, int):
        years = [f'{year:04d}']
    elif isinstance(year, str):
        years = [year]
    elif year is None:
        years = ['*']
    else:
        years = []

    if isinstance(month, (list, tuple)):
        months = [f'{m:02d}' for m in month]
    elif isinstance(month, int):
        months = [f'{month:02d}']
    elif isinstance(month, str):
        months = [month]
    elif month is None:
        months = ['*']
    else:
        months = []

    dfs = []
    for yr in years:
        for mo in months:
            s3uri = f's3://anaconda-package-data/conda/hourly/{yr}/{mo}/*-*-*.parquet'
            df = dd.read_parquet(
                s3uri,
                storage_options={'anon': True},
                engine='pyarrow',
            )
            if 'pkg_name' not in df:
                continue

            df = df[['time', 'data_source', 'pkg_name', 'counts']]
            df = df.loc[df.pkg_name.isin(packages)].compute()
            df.pkg_name = df.pkg_name.cat.remove_unused_categories()
            df = df.groupby([df.time.dt.to_period('M'), df.pkg_name]).sum().reset_index()
            df = df.pivot(index='time', columns='pkg_name', values='counts')
            df.index.name = 'month'
            dfs.append(df)

    if dfs:
        return pd.concat(dfs).fillna(0).astype('int64')
    else:
        return None


if __name__ == '__main__':
    repos = read_repos_file()
    packages = get_packages(repos, kind='conda')

    STATS_FILE = Path(__file__).with_suffix('.csv')
    if STATS_FILE.exists():
        print('Updating Conda stats...')
        df = read_stats_file(STATS_FILE)
        df = update_stats(df, packages=packages, method=get_conda_stats)
    else:
        print('Downloading all Conda stats...')
        df = get_conda_stats(packages=packages)

    df.to_csv(STATS_FILE)
