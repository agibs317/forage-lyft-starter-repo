from abc import ABC


class Tire(ABC):

    @abstractmethod
    def needs_service(self):
        pass
