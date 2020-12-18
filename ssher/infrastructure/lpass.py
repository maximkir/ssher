from ssher.core import entities
from ssher.infrastructure.os import OS


class LastPassIdentityKey(entities.IdentityKey):
    def __init__(self, username: str, key_entry: str, os_runner: OS):
        self._username = username
        # TODO: ensure that the entry exists inside the vault
        self._key_entry = key_entry
        self._os_runner = os_runner
        self._identity_key = None
        self._passphrase = None

    def load(self):
        note_type = self._read_entry_field("NoteType").strip()
        assert note_type == "SSH Key", "Only SSH Key note type supported!"
        self._identity_key = self._read_entry_field("Private Key").strip()
        self._passphrase = self._read_entry_field("Passphrase").strip()
        print(
            f"Identity key details loaded successfully from last pass entry: {self._key_entry}"
        )

    def passphrase(self):
        return self._passphrase

    def key(self):
        return self._identity_key

    def _login(self):
        while not self._is_logged_in():
            self._os_runner.spawn_child_interact(
                f"lpass login --color=never {self._username}"
            )

    def _is_logged_in(self):
        return f"Logged in as {self._username}." in self._os_runner.spawn_child_read(
            "lpass status --color=never"
        )

    def _read_entry_field(self, field):
        return self._os_runner.pexpect_spawn_read(
            f'lpass show --color=never --field="{field}" {self._key_entry}'
        )
