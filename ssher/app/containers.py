from ssher.core import use_cases, entities
from ssher.infrastructure import os, lpass

from dependency_injector import containers, providers


class AppContainer(containers.DeclarativeContainer):

    config = providers.Configuration()

    os_runner = providers.Singleton(os.CmdRunner)

    identity_key_store = providers.Selector(

        lpass=providers.Factory(lpass.LastPassIdentityKey),
        default=providers.Factory(entities.IdentityKey)
    )

    ssh_connection = providers.Factory(use_cases.EstablishSshConnection, os_runner=os_runner)
