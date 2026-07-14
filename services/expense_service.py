from datetime import datetime
from models.expense import Expense


class ExpenseService:
    @staticmethod
    def create_expense(ad, tutar, kategori):
        tarih = datetime.now().strftime("%Y-%m-%d")
        return Expense(ad, tutar, kategori, tarih)

    @staticmethod
    def get_total(expenses):
        return sum(expense.tutar for expense in expenses)

    @staticmethod
    def filter_by_category(expenses, kategori):
        return [
            expense for expense in expenses
            if expense.kategori.lower() == kategori.lower()
        ]

    @staticmethod
    def get_monthly_total(expenses, month):
        total = 0

        for expense in expenses:
            if expense.tarih.startswith(month):
                total += expense.tutar

        return total

    @staticmethod
    def get_max_expense(expenses):
        if len(expenses) == 0:
            return None

        return max(expenses, key=lambda expense: expense.tutar)

    @staticmethod
    def group_by_category(expenses):
        categories = {}

        for expense in expenses:
            if expense.kategori in categories:
                categories[expense.kategori] += expense.tutar
            else:
                categories[expense.kategori] = expense.tutar

        return categories

    @staticmethod
    def is_budget_exceeded(expenses, budget):
        total = ExpenseService.get_total(expenses)
        return budget > 0 and total > budget