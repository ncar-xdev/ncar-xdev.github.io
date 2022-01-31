"""
This file contains a function to read data from a public AWS S3 store containing hourly
Conda package download data.
"""

import dask.dataframe as dd


def get_conda_stats_for_month(packages=[], year=2022, month=1):
    if not packages:
        return None

    s3uri = f's3://anaconda-package-data/conda/hourly/{year:04d}/{month:02d}/{year:04d}-{month:02d}-*.parquet'
    df = dd.read_parquet(
        s3uri,
        columns=['time', 'data_source', 'pkg_name', 'counts'],
        storage_options={'anon': True},
        engine='pyarrow',
    )

    df = df.loc[df.pkg_name.isin(['intake-esm', 'jupyter-forward', 'ncar-jobqueue'])].compute()
    df.pkg_name = df.pkg_name.cat.remove_unused_categories()
    df = df.groupby([df.time.dt.to_period('M'), df.pkg_name]).sum().reset_index()
    df = df.pivot(index='time', columns='pkg_name', values='counts')
    df.index.name = 'month'

    return df
