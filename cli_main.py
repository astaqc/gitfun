import subprocess
from github import Github
import click
import argparse
from gitfun import GitFun as gf

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

# @cli.command()
# @click.option('-url', type=str, help='Paste your link of the repo')
# @click.option('-m',type=str,help = "Commit message ")
# @click.option('-b',type=str, help ="Branch name for checkout")
# #
# def initpush(url,m):
#     click.echo(gf.init_push())


@cli.command()
def status():
    click.echo(gf.status())

@cli.command()
@click.option('-url', type=str, help='Paste your link of the repo')
@click.option('-m',type=str,help = "Commit message ")
@click.option('-b',type=str, help ="Branch name for checkout")
def pushbranch(url,m,b):
    click.echo(gf.push_branch(url,m,b))