from abc import ABC, abstractmethod


class IOffsiteCourse(ABC):
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def __str__(self):
        pass
