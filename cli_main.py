import subprocess
from github import Github
import click
import argparse
from gitfun import GitFun as gf

@click.group(context_settings=CONTEXT_SETTINGS)
def cli():
    pass

@cli.command()
@click.option('-url', type=str, help='Length of password to be generated')

def fungit(url):
    click.echo(gf.remote(url))