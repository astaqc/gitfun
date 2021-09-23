import subprocess
import click
from gitfun import GitFun as gf

CONTEXT_SETTINGS = dict(help_option_names=['-h', '--help'])
@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass




@cli.command()
def status():
    click.echo(gf.status())

@cli.command()
@click.option('-url', type=str, help='Paste your link of the repo')
@click.option('-m',type=str,help = "Commit message ")
@click.option('-b',type=str, help ="Branch name for checkout")
def pushbranch(url,m,b):
    click.echo(gf.push_branch(url,m,b))

@cli.command()
def remote():
    click.echo(gf.remote())

@cli.command()
@click.option('-url', type=str, help='Paste your link of the repo')
@click.option('-m',type=str,help = "Commit message ")
@click.option('-b',type=str, help ="Branch name for checkout")
def privaterepo():
    subprocess.getoutput('echo enter the github access token"')
    token = input()
    click.echo(gf.push_private_repo(token))

