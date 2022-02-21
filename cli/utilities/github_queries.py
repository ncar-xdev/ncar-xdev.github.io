import requests

import pandas as pd


def get_all_repos_info(repos={}, token=None):
    if len(repos) == 0:
        return None

    repo_queries = []
    for key, val in repos.items():
        pkg = key.replace('-', '_')
        owner = val['org']
        name = val['repo']

        repo_queries.append(
            f'  {pkg}: repository(owner: "{owner}", name: "{name}") {{ ...repoInfo }}'
        )
    queries = '\n'.join(repo_queries)

    query = f"""
fragment repoInfo on Repository {{
  forkCount
  latestRelease {{
    tag {{
      name
    }}
  }}
  stargazerCount
  watchers {{
    totalCount
  }}
}}

{{
{queries}
}}
"""

    url = 'https://api.github.com/graphql'
    json = {'query': query}
    headers = {'Authorization': f'bearer {token}'}
    response = requests.post(url, json=json, headers=headers)
    if response.status_code != 200:
        raise RuntimeError(f'Failed to read project data [{response.status_code}]')
    response_data = response.json()

    df = pd.DataFrame()
    for pkg in response_data['data']:
        data = {}
        data['package'] = pkg
        data['forks'] = response_data['data'][pkg]['forkCount']
        if response_data['data'][pkg]['latestRelease']:
            data['release'] = response_data['data'][pkg]['latestRelease']['tag']['name']
        else:
            data['release'] = None
        data['stargazers'] = response_data['data'][pkg]['stargazerCount']
        data['watchers'] = response_data['data'][pkg]['watchers']['totalCount']
        df = df.append(data, ignore_index=True)

    df = df.astype(dtype={'forks': 'int64', 'stargazers': 'int64', 'watchers': 'int64'})

    return df


def get_repo_commits(owner=None, name=None, token=None):
    if owner is None or name is None:
        return None

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}

    after = None
    has_next_page = True
    df = pd.DataFrame()
    while has_next_page:
        after_str = '' if after is None else f', after: "{after}"'
        query = f"""
query {{
  repository(owner: "{owner}", name: "{name}") {{
    defaultBranchRef {{
      target {{
        ... on Commit {{
          history(first: 100{after_str}) {{
            pageInfo {{
              endCursor
              hasNextPage
            }}
            edges {{
              node {{
                additions
                committedDate
                deletions
                author {{
                  user {{
                    login
                  }}
                }}
              }}
            }}
          }}
        }}
      }}
    }}
  }}
}}
"""

        json = {'query': query}
        response = requests.post(url, json=json, headers=headers)
        if response.status_code != 200:
            raise RuntimeError(f'Failed to read project data [{response.status}]')
        response_json = response.json()
        default_branch_data = response_json['data']['repository']['defaultBranchRef']
        history_data = default_branch_data['target']['history']

        after = history_data['pageInfo']['endCursor']
        has_next_page = history_data['pageInfo']['hasNextPage']

        for node in history_data['edges']:
            data = {}
            data['package'] = name
            data['additions'] = node['node']['additions']
            data['deletions'] = node['node']['deletions']
            data['date'] = node['node']['committedDate']
            user = node['node']['author']['user']
            if user:
                data['author'] = user['login']
            df = df.append(data, ignore_index=True)

    df = df.astype(dtype={'additions': 'int64', 'deletions': 'int64'})

    return df


def get_repo_issues(owner=None, name=None, token=None):
    if owner is None or name is None:
        return None

    url = 'https://api.github.com/graphql'
    headers = {'Authorization': f'bearer {token}'}

    after = None
    has_next_page = True
    df = pd.DataFrame(columns=['package', 'number', 'created', 'closed', 'author'])
    while has_next_page:
        after_str = '' if after is None else f', after: "{after}"'
        query = f"""
query {{
  repository(owner: "{owner}", name: "{name}") {{
    issues(first: 100{after_str}) {{
      pageInfo {{
        endCursor
        hasNextPage
      }}
      edges {{
        node {{
          number
          createdAt
          closedAt
          author {{
            login
          }}
        }}
      }}
    }}
  }}
}}
"""

        json = {'query': query}
        response = requests.post(url, json=json, headers=headers)
        if response.status_code != 200:
            raise RuntimeError(f'Failed to read project data [{response.status}]')
        response_data = response.json()
        issue_data = response_data['data']['repository']['issues']

        after = issue_data['pageInfo']['endCursor']
        has_next_page = issue_data['pageInfo']['hasNextPage']

        for node in issue_data['edges']:
            data = {}
            data['package'] = name
            data['number'] = node['node']['number']
            data['created'] = node['node']['createdAt']
            data['closed'] = node['node']['closedAt']
            data['author'] = node['node']['author']['login']
            df = df.append(data, ignore_index=True)

    return df
