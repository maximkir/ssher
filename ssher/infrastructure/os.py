from ssher.core.ports.outgoing import OS

import pexpect


class CmdRunner(OS):
    def spawn_child_interact(self, *args, **kwargs):
        self._spawn_child(*args, **kwargs).interact()

    def spawn_child_read(self, *args, **kwargs):
        return self._spawn_child(*args, **kwargs).read()

    def _spawn_child(self, *args, **kwargs):
        kwargs.setdefault("encoding", "utf-8")
        return pexpect.spawn(*args, **kwargs)
