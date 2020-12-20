from dataclasses import dataclass


@dataclass
class IdentityKey:

    key: str = None
    passphrase: str = None

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    def load(self):
        ...

    def local_path(self):
        ...
