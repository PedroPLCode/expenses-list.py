import json

class Expenses:
    def __init__(self):
        try:
            with open("expenses.json", "r") as filename:
                self.expenses = json.load(filename)
        except FileNotFoundError:
            self.expenses = []

    def all(self):
        return self.expenses
    
    def get(self, id):
        expense = [expense for expense in self.all() if expense['id'] == id]
        if expense:
            return expense[0]
        return []
    
    def get_expenses_filtered_by_paid(self, is_paid):
        filtered = [expense for expense in self.all() if expense['paid'] == is_paid]
        if filtered:
            return filtered
        return []
    
    def create(self, data):
        data['id'] = expenses.all()[-1]['id'] + 1
        self.expenses.append(data)
        self.save_all()
        
    def delete(self, id):
        expense = self.get(id)
        if expense:
            self.expenses.remove(expense)
            self.save_all()
            return True
        return False

    def save_all(self):
        with open("expenses.json", "w") as filename:
            json.dump(self.expenses, filename)

    def update(self, id, data):
        expense = self.get(id)
        if expense:
            data['id'] = id
            index = self.expenses.index(expense)
            self.expenses[index] = data
            self.save_all()
            return True
        return False

expenses = Expenses()