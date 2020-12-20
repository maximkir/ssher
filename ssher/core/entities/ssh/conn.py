from ssher.core.ports.outgoing import OS

from dataclasses import dataclass
from pexpect import pxssh


@dataclass(frozen=True)
class ShhConnection:
    username: str
    hostname: str
    port: int
    os: OS  # TODO: replace with a SSH class...

    def connect(self):
        self.os.spawn_child(
            "/bin/bash",
            [
                "-c",
                f"ssh -p {self.port} -l {self.username} {self.hostname}",
            ],
        )

    def can_login(self):
        s = pxssh.pxssh(
            options={
                "StrictHostKeyChecking": "no",
                "LogLevel": "ERROR",
            }
        )
        try:
            return s.login(
                self.hostname,
                username=self.username,
                password="password",
                port=self.port,
                quiet=False,
            )
        except pxssh.ExceptionPxssh as exp:
            print(exp)
            return False


