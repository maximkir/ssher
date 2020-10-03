from .containers import AppContainer

from pathlib import Path
import click

DEFAULT_CONFIG_PATH = f"{Path.home()}/.ssher/config.yaml"


@click.command()
@click.argument("hostname", type=click.STRING)
@click.option("-u", "--username")
@click.option("-c", "--config", default=DEFAULT_CONFIG_PATH)
def connect(hostname, username, config):
    click.echo(f"Connecting to {username}@{hostname}")

    container = AppContainer()
    container.config.from_yaml(config)

    # identity key factory

    print(container.config()[hostname])

    container.ssh_connection(
        username=username,
        hostname=hostname,
    ).create()
