from ssher.ssh.conn import Connection

import click


@click.command()
@click.argument("hostname", type=click.STRING)
@click.option("-u", "--username")
def connect(hostname, username):
    click.echo(f"Connecting to {username}@{hostname}")
    Connection(username=username, hostname=hostname).connect()
