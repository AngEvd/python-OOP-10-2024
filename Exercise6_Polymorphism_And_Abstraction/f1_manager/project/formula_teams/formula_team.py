from abc import ABC, abstractmethod


class FormulaTeam(ABC):
    def __init__(self, budget: int) -> None:
        self.budget = budget

    @property
    def budget(self) -> int:
        return self.__budget

    @budget.setter
    def budget(self, value: int) -> None:
        if value < 1_000_000:
            raise ValueError("F1 is an expensive sport, find more sponsors!")
        self.__budget = value

    @property
    @abstractmethod
    def PRIZE_MONEY(self):
        pass

    @property
    @abstractmethod
    def EXPENSES(self):
        pass

    def calculate_revenue_after_race(self, race_pos: int) -> str:
        prize_money, revenue = 0, 0
        for sponsor in self.PRIZE_MONEY.values():
            for pos in sponsor:
                if race_pos <= pos:
                    revenue += sponsor[pos]
                    break
        revenue -= self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
