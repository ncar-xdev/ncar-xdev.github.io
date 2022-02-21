#!/usr/bin/env python
from datetime import datetime
from pathlib import Path
import yaml

ROOT_DIR = Path(__file__).parent.parent


def get_tutorials_data():
    with open(ROOT_DIR / 'data/tutorials.yml') as f:
        data = yaml.safe_load(f)
    data = sorted(data, key=lambda x: x['Date'], reverse=True)

    for item in data:
        dt = datetime.strptime(item['Date'], '%Y-%m-%d')
        item['Date'] = dt

    return data


def make_tutorial_markdown():
    tutorials_md = """# Python Tutorials

Below you will see all of our past and upcoming tutorials as part of our
Python Tutorial Seminars.  All of these tutorials are recorded and the videos
are hosted for free viewing on YouTube as part of the
[ProjectPythia channel](https://www.youtube.com/channel/UCoZPBqJal5uKpO8ZiwzavCw).
Our upcoming tutorials can also be viewed on the
[ESDS Python Training page](https://ncar.github.io/esds/calendar/#python-training).

"""
    tutorials = get_tutorials_data()

    for tutorial in tutorials:
        title = tutorial['Title']
        dt = tutorial['Date']
        date = f"**Date:** {dt.strftime('%Y %B %-d')}"
        if dt > datetime.now():
            date += ' <span class="badge badge-warning">UPCOMING</span>'
        date += '<br>'
        if 'Attendance' in tutorial:
            attendance = f"**Number of Attendees:** {tutorial['Attendance']}<br>"
        else:
            attendance = ''
        if 'Post' in tutorial:
            post = f"**Original Posting:** {tutorial['Post']}<br>"
        else:
            post = ''
        if 'Content' in tutorial:
            content = f"**Tutorial Data:** {tutorial['Content']}<br>"
        else:
            content = ''
        if 'Video' in tutorial:
            video = f"**Video Recording:** {tutorial['Video']}<br>"
        else:
            video = ''
        if 'FAQ' in tutorial:
            faq = f"**Q/A:** {tutorial['FAQ']}<br>"
        else:
            faq = ''

        tutorials_md += f"""
## {title}

{date}{post}{content}{video}{faq}{attendance}
"""

    with open(ROOT_DIR / 'status/tutorials.md', 'w') as f:
        f.write(tutorials_md)


if __name__ == '__main__':
    make_tutorial_markdown()
