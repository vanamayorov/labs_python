from abc import ABC, abstractmethod


class ILocalCourse(ABC):
    """The interface of the local course in the software academy."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
