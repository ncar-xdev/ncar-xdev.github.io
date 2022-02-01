from pathlib import Path
import yaml


def parse_github_string(gh_string):
    try:
        gh_org, gh_repo = gh_string.split('/', 1)
    except ValueError:
        gh_org = None
        gh_repo = None
    return gh_org, gh_repo


def read_repos_file():
    filename = Path(__file__).with_suffix('.yml')
    with open(filename) as yml:
        _repos = yaml.safe_load(yml)

    repos = {}
    for repo in _repos:
        gh_org = None
        gh_repo = None
        if isinstance(_repos[repo], str):
            gh_org, gh_repo = parse_github_string(_repos[repo])
            pypi_pkg = gh_repo
            conda_pkg = gh_repo
        elif isinstance(_repos[repo], dict):
            if 'github' in _repos[repo]:
                gh = _repos[repo]['github']
                if isinstance(gh, str):
                    gh_org, gh_repo = parse_github_string(gh)
                elif isinstance(gh, dict):
                    gh_org = gh.get('org', None)
                    gh_repo = gh.get('repo', None)
            pypi_pkg = _repos[repo]['pypi'] if 'pypi' in _repos[repo] else gh_repo
            conda_pkg = _repos[repo]['conda'] if 'conda' in _repos[repo] else gh_repo

        repos[repo] = dict(org=gh_org, repo=gh_repo, pypi=pypi_pkg, conda=conda_pkg)

    return repos


def get_packages(repos, kind='pypi'):
    packages = []
    for repo in repos:
        if kind in repos[repo] and repos[repo][kind]:
            packages.append(repos[repo][kind])
    return packages
