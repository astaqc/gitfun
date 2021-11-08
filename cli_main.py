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
def status():
    click.echo(gf.status())

@cli.command()
@click.option('-url', type=str, help='Paste your link of the repo',required=False)
@click.option('-m',type=str,help = "Commit message ")
@click.option('-b',type=str, help ="Branch name for checkout")

def pushbranch(m,b,url):
    click.echo(gf.push_branch(m,b,url))

@cli.command()
def remote():
    click.echo(gf.remote())

if __name__ == '__main__':
    cli()