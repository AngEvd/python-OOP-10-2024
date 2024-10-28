from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES = 200_000
    PRIZE_MONEY = {
        "Petronas": {
            1: 1_000_000,
            3: 500_000
        },
        "TeamViewer": {
            5: 100_000,
            7: 50_000
        }
    }

    def __init__(self, budget: int):
        super().__init__(budget)
