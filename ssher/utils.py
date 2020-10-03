
import pexpect


def pexpect_run(*args, **kwargs):
    kwargs.setdefault("encoding", "utf-8")
    return pexpect.run(*args, **kwargs)

