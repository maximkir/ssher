
class IdentityKey:

    key: str
    passphrase: str

    def __enter__(self):
        ...

    def __exit__(self, exc_type, exc_val, exc_tb):
        ...

    def load(self):
        ...

    def local_path(self):
        ...
