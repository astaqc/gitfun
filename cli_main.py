import subprocess
from github import Github
import click
import argparse
from gitfun import GitFun as gf
CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-url', type=str, help='Paste your link of the repo')

def initpush(url):
    click.echo(gf.init_push(url))