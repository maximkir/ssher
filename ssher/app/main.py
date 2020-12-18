from .containers import AppContainer
from ssher.core.entities import IdentityKey

import sys
from pathlib import Path
import click

DEFAULT_CONFIG_PATH = f"{Path.home()}/.ssher/config.yaml"


@click.command()
@click.argument("hostname", type=click.STRING)
@click.option(
    "-l",
    "--username",
    envvar="USERNAME",
    help="Specifies the user to log in as on the remote machine",
)
@click.option(
    "-p",
    "--port",
    type=click.INT,
    default=22,
    help="Port to connect to on the remote host",
)
@click.option("-c", "--config", default=DEFAULT_CONFIG_PATH)
def connect(hostname, username, port, config):
    click.echo(f"Connecting to {username}@{hostname}")

    container = AppContainer()
    container.config.from_yaml(config)
    identity_key = IdentityKey()
    if hostname in container.config():
        pass
    connection = container.ssh_connection(
        username=username, hostname=hostname, port=port, identity_key=identity_key
    ).create()

    # connection.connect()
    if not connection.can_login():
        sys.exit(-1)
