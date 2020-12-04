import abc


class BettingStrategy:
    def bet(self):
        raise NotImplementedError("No bet method")

    def record_win(self):
        pass

    def record_loss(self):
        pass


class Flat(BettingStrategy):
    def bet(self):
        return 1


class BettingStrategy2(metaclass=abc.ABCMeta):

    @abstractmethod
    def bet(self):
        return 1

    def record_win(self):
        pass

    def record_loss(self):
        pass
