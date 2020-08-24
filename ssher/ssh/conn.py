import pexpect


class Connection:

    def __init__(self, username, hostname):
        self._username = username
        self._hostname = hostname

    def connect(self):
        cmd = f"ssh {self._username}@{self._hostname}"
        pexpect.spawn(cmd).interact()
