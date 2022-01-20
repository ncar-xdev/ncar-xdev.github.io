#!/usr/bin/env python
from google.cloud import bigquery

client = bigquery.Client()

pkgs = [
    'intake-esm',
    'jupyter-forward',
    'ncar-jobqueue',
]

pkg_string = ', '.join(f"'{p}'" for p in pkgs)
pkg_query_list = []
for i, p in enumerate(pkgs):
    pkg_query_list.append(f"SUM(CASE WHEN file.project = '{p}' THEN 1 ELSE 0 END) AS `pkg{i}`")
pkg_queries = ',\n    '.join(pkg_query_list)

query = f"""
SELECT
    FORMAT_DATE("%Y-%m", DATE(timestamp)) as `month`,
    {pkg_queries}
FROM `bigquery-public-data.pypi.file_downloads`
WHERE
    file.project in ({pkg_string})
    AND DATE(timestamp) > '2018-01-01'
GROUP BY `month`
ORDER BY `month` ASC
"""

headings = ('month',) + tuple(p for p in pkgs)
print(*headings)

query_job = client.query(query)
results = query_job.result()
for row in results:
    vals = (row.month,) + tuple(row.get(f'pkg{i}') for i in range(len(pkgs)))
    print(*vals)
