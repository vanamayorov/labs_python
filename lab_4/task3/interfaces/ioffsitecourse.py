from abc import ABC, abstractmethod


class IOffsiteCourse(ABC):
    """The interface of the offsite course in the software academy."""
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
