from ssher import utils

import os
from pathlib import Path
import click

DEFAULT_CONFIG_PATH = f"{Path.home()}/.ssher/config.yaml"


@click.command()
@click.argument("hostname", type=click.STRING)
@click.option("-u", "--username")
@click.option("-c", "--config", default=DEFAULT_CONFIG_PATH)
def connect(hostname, username, config):
    click.echo(f"Connecting to {username}@{hostname}")
    config = utils.load_config(config)
    if hostname in config:
        utils.load_identity_key()
        

        identity_key_path = os.path.expanduser(config[hostname]["identity-key-path"])
        loader_cls = KEY_LOADER_REGISTRY[config[hostname]["identity-key-plugin"]["name"]]

        with loader_cls(**config[hostname]["identity-key-plugin"]) as identity_key:
            with open(identity_key_path, "w") as key_path:
                key_path.write(identity_key.key())

        utils.pexpect_spawn(f"ssh-add -t 1h {identity_key_path}").interact()
    Connection(username=username, hostname=hostname).connect()
