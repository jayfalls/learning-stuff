from abc import ABC, abstractmethod

class Trader(ABC):
    @staticmethod
    def get_stocks() -> tuple:
        return (10, 12, 12, 24)

    @staticmethod
    @abstractmethod
    def should_sell(stocks: tuple) -> bool:
        pass

    @staticmethod
    @abstractmethod
    def should_buy(stocks: tuple) -> bool:
        pass

    def determine_trade(self) -> None:
        stocks: tuple = self.get_stocks()
        if self.should_sell(stocks):
            print("Should Sell")
        if self.should_buy(stocks):
            print("Should Buy")

class AverageTrader(Trader):
    @staticmethod
    def should_sell(stocks: tuple) -> bool:
        return True

    @staticmethod
    def should_buy(stocks: tuple) -> bool:
        return True

class MinMaxTrader(Trader):
    @staticmethod
    def should_sell(stocks: tuple) -> bool:
        return False

    @staticmethod
    def should_buy(stocks: tuple) -> bool:
        return True


minmax = MinMaxTrader()
average = AverageTrader()

minmax.determine_trade()
average.determine_trade()
