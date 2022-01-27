"""
This file contains a simple function to read data from Google BigQuery (i.e., via SQL).
To access Google BigQuery, you need a Google Cloud Project with the BigQuery API
enabled.  (Note, you cannot do this with your NCAR Google account!)  Once you have
a BigQuery-enabled GC project, you can download credentials to your laptop/machine as
a JSON, and you can set the environment variable:

GOOGLE_APPLICATION_CREDENTIALS="path/to/credentials.json"

Without the credentials file AND this environment variable set, this funciton will
fail with authentication errors.
"""

from calendar import monthrange

from google.cloud import bigquery


def get_pypi_stats_for_month(packages=[], year=2022, month=1):
    if not packages:
        return None

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
        AND DATE(timestamp) >= '{year:04d}-{month:02d}-01'
        AND DATE(timestamp) <= '{year:04d}-{month:02d}-{monthrange(year, month)[1]:02d}'
    GROUP BY `month`
    ORDER BY `month` ASC
    """

    df = client.query(sql).to_dataframe()
    df.rename(columns={f'p{i}':p for i,p in enumerate(packages)}, inplace=True)
    df = df.set_index('month')
    df.columns.name = 'pkg_name'

    return df
