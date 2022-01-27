#!/usr/bin/env python
from datetime import datetime

from condastats import get_conda_stats_for_month
from pypistats import get_pypi_stats_for_month
from xdevrepos import read_repos_file, get_packages


def get_download_stats(repos={}, year=2022, month=1):
    if not repos:
        return

    pypi_pkgs = get_packages(repos, kind='pypi')
    df_pypi = get_pypi_stats_for_month(packages=pypi_pkgs, year=year, month=month)
    print(df_pypi)

    conda_pkgs = get_packages(repos, kind='conda')
    df_conda = get_conda_stats_for_month(packages=conda_pkgs, year=year, month=month)
    print(df_conda)


if __name__ == '__main__':
    now = datetime.now()
    repos = read_repos_file()
    get_download_stats(repos=repos, year=2021, month=12)
