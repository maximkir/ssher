from ssher.core.entities import IdentityKey, ShhConnection
from ssher.core.ports.outgoing import OS

from dataclasses import dataclass


@dataclass(frozen=True)
class EstablishSshConnection:
    username: str
    hostname: str
    identity_key: IdentityKey
    os_runner: OS
    port: int = 22

    def create(self):
        with self.identity_key:
            return ShhConnection(
                username=self.username,
                hostname=self.hostname,
                os=self.os_runner,
                port=self.port,
            )
