import abc


# TODO: consider to create something more specific
class OS(abc.ABC):
    @abc.abstractmethod
    def spawn_child(*args, **kwargs):
        ...
