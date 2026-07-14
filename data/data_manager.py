import json
from models.expense import Expense


class DataManager:
    EXPENSE_FILE = "harcamalar.json"
    SETTINGS_FILE = "settings.json"

    @staticmethod
    def load_expenses():
        try:
            with open(DataManager.EXPENSE_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return [Expense.from_dict(item) for item in data]
        except FileNotFoundError:
            return []

    @staticmethod
    def save_expenses(expenses):
        with open(DataManager.EXPENSE_FILE, "w", encoding="utf-8") as file:
            json.dump(
                [expense.to_dict() for expense in expenses],
                file,
                ensure_ascii=False,
                indent=4
            )

    @staticmethod
    def load_budget():
        try:
            with open(DataManager.SETTINGS_FILE, "r", encoding="utf-8") as file:
                data = json.load(file)
                return data.get("budget", 0)
        except FileNotFoundError:
            return 0

    @staticmethod
    def save_budget(budget):
        with open(DataManager.SETTINGS_FILE, "w", encoding="utf-8") as file:
            json.dump(
                {"budget": budget},
                file,
                ensure_ascii=False,
                indent=4
            )