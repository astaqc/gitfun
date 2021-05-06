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
@click.option('-m',type=str,help = "Commit message ")

def initpush(url,m):
    click.echo(gf.init_push(url,m))


@cli.command()
def status():
    click.echo(gf.status())