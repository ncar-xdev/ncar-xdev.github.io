#!/usr/bin/env python
from calendar import monthrange
from pathlib import Path

from google.cloud import bigquery
import pandas as pd

from common import update_stats, read_stats_file
from xdevrepos import read_repos_file, get_packages


def get_pypi_stats(packages=[], year=None, month=None):
    """
    Read PyPI download statistics from Google BigQuery
    """
    if not packages:
        return None

    if isinstance(year, (list, tuple)):
        year1, year2 = min(year), max(year)
    elif year is None:
        year1, year2 = 2018, 2030
    else:
        year1 = year2 = year

    if isinstance(month, (list, tuple)):
        month1, month2 = min(month), max(month)
    elif month is None:
        month1, month2 = 1, 12
    else:
        month1 = month2 = month

    day1, day2 = 1, monthrange(year2, month2)[1]

    client = bigquery.Client()

    pkg_string = ', '.join(f"'{p}'" for p in packages)

    pkg_query_list = []
    for i, p in enumerate(packages):
        pkg_query_list.append(f"SUM(CASE WHEN file.project = '{p}' THEN 1 ELSE 0 END) AS `p{i}`")
    pkg_queries = ',\n    '.join(pkg_query_list)

    sql = f"""
    SELECT
        FORMAT_DATE("%Y-%m", DATE(timestamp)) as `month`,
        {pkg_queries}
    FROM `bigquery-public-data.pypi.file_downloads`
    WHERE
        file.project in ({pkg_string})
        AND DATE(timestamp) >= '{year1:04d}-{month1:02d}-{day1:02d}'
        AND DATE(timestamp) <= '{year2:04d}-{month2:02d}-{day2:02d}'
    GROUP BY `month`
    ORDER BY `month` ASC
    """

    df = client.query(sql).to_dataframe()
    df = df.rename(columns={f'p{i}':p for i,p in enumerate(packages)})
    df['month'] = pd.to_datetime(df.month).dt.to_period('M')
    df.columns.name = 'pkg_name'
    df = df.set_index('month')

    return df


if __name__ == '__main__':
    repos = read_repos_file()
    packages = get_packages(repos, kind='pypi')

    STATS_FILE = Path(__file__).with_suffix('.csv')
    if STATS_FILE.exists():
        print('Updating PyPI stats...')
        df = read_stats_file(STATS_FILE)
        df = update_stats(df, packages=packages, method=get_pypi_stats)
    else:
        print('Downloading all PyPI stats...')
        df = get_pypi_stats(packages=packages)

    df.to_csv(STATS_FILE)
