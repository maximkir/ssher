import abc


# TODO: consider to create something more specific
class OS(abc.ABC):
    @abc.abstractmethod
    def spawn_child_interact(self, *args, **kwargs):
        ...

    @abc.abstractmethod
    def spawn_child_read(self, *args, **kwargs):
        ...
