from ssher.core.ports.outgoing import OS

import pexpect


class CmdRunner(OS):

    def spawn_child(*args, **kwargs):
        kwargs.setdefault("encoding", "utf-8")
        return pexpect.spawn(*args, **kwargs).interact()
