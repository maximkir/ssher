from ssher.core.ports.outgoing import OS

from dataclasses import dataclass


@dataclass(frozen=True)
class ShhConnection:
    username: str
    hostname: str
    os: OS

    def connect(self):
        cmd = f"ssh {self._username}@{self._hostname}"
        self.os.spawn_child(cmd)
