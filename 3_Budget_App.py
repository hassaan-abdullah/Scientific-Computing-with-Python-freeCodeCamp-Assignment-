class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        output_string = f'{self.name:*^30}'

        for item in self.ledger:
            output_string += f'\n{item["description"][:23]:23}{item["amount"]:>7.2f}'

        output_string += f'\nTotal: {self.get_balance():.2f}'

        return output_string

    def deposit(self, amount, description=''):
        self.ledger.append({'amount' : amount, 'description' : description})

    def withdraw(self, amount, description=''):
        if self.check_funds(amount):
            self.ledger.append({'amount' : -amount, 'description' : description})
            return True
        return False

    def get_balance(self):
        balance = 0
        for item in self.ledger:
            balance += item['amount'] 
        return balance

    def transfer(self, amount, other_category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {other_category.name}')
            other_category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount <= self.get_balance():
            return True
        return False

def create_spend_chart(categories):
    chart_to_print = ''
    
    spent_per_category = [sum(-item['amount'] for item in category.ledger if item['amount'] < 0) for category in categories]
    total_spent = sum(spent_per_category)
    spent_percentage = [(((spent / total_spent) * 100) // 10) * 10 for spent in spent_per_category]

    chart_to_print += '\nPercentage spent by category\n'

    for percent in range(100, -10, -10):
        chart_to_print += f'{percent:>3}| '
        for spent in spent_percentage:
            if spent >= percent:
                chart_to_print += 'o  '
            else:
                chart_to_print += ' ' * 3
                
        chart_to_print += '\n'
    
    chart_to_print += ' ' * 4 + '-' * (1 + 3 * len(categories))

    longest_category_name_length = len(max([category.name for category in categories], key = len))
    
    for i in range(longest_category_name_length):
        chart_to_print += '\n'
        chart_to_print += ' ' * 5
        for category in categories:
            if i < len(category.name):
                chart_to_print += category.name[i] + ' ' * 2
            else:
                chart_to_print += ' ' * 3
    
    return chart_to_print

food = Category("Food")
food.deposit(1000, "initial deposit")
food.withdraw(10.15, "groceries")
food.withdraw(15.89, "restaurant and more food for dessert")
print(food.get_balance())
clothing = Category("Clothing")
food.transfer(50, clothing)
clothing.withdraw(25.55)
clothing.withdraw(100)
auto = Category("Auto")
auto.deposit(1000, "initial deposit")
auto.withdraw(15)

print(food)
print(clothing)

print(create_spend_chart([food, clothing, auto]))