#!/usr/bin/env python
from pathlib import Path
import yaml

import click
import pandas as pd


@click.command()
@click.argument('csvfile', type=click.Path(exists=True))
def main(csvfile):
    df = pd.read_csv(csvfile, dtype={'Attendance': 'Int64', 'Date': str})

    ymldata = [row.dropna().to_dict() for _, row in df.iterrows()]
    ymlfile = Path(csvfile).with_suffix('.yml')
    with open(ymlfile, 'w') as ymlf:
        yaml.dump(ymldata, ymlf, indent=2)


if __name__ == '__main__':
    main()
