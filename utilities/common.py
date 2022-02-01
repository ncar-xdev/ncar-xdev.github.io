from datetime import datetime

from dateutil.relativedelta import relativedelta
import pandas as pd


def read_stats_file(filename):
    df = pd.read_csv(filename)
    df['month'] = pd.to_datetime(df.month).dt.to_period('M')
    df = df.set_index('month')

    return df


def update_stats(df, packages=[], n=3, method=None):
    if method is None:
        raise ValueError('method is not set.  Needs to be a function to download statistics.')

    now = datetime.now()
    for i in range(n):
        dt = now - relativedelta(months=i)
        year, month = dt.year, dt.month
        df_update = method(packages=packages, year=year, month=month)
        _update_dataframe(df, df_update)

    return df


def _update_dataframe(df1, df2):
    if df2 is None:
        return df1

    for col in df2:
        if col not in df1:
            df1[col] = 0

    for row in df2.itertuples():
        idx = row.Index
        vals = {}
        for k, v in row._asdict().items():
            if k == 'Index':
                continue
            if k[0] == '_':
                k = df2.columns[int(k[1:])-1]
            vals[k] = v
        df1.loc[idx] = vals
