class MoneyMachine:

    CURRENCY = "$"

    COIN_VALUES = {
        "quarters": 0.25,
        "dimes": 0.10,
        "nickles": 0.05,
        "pennies": 0.01
    }

    def __init__(self):
        self.profit = 0
        self.money_received = 0

    def report(self):
        """Prints the current profit"""
        print(f"Money: {self.CURRENCY}{self.profit}")

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        self.money_received = 0  # Reset to avoid accumulation
        try:
            for coin in self.COIN_VALUES:
                count = input(f"How many {coin}?: ")
                self.money_received += int(count) * self.COIN_VALUES[coin]
            return self.money_received
        except ValueError:
            print("Invalid input. Please enter whole numbers for coins.")
            self.money_received = 0
            return 0


    def make_payment(self, cost):
            """Returns True when payment is accepted, or False if insufficient."""
            self.process_coins()
            if self.money_received >= cost:
                change = round(self.money_received - cost, 2)
                print(f"Here is {self.CURRENCY}{change} in change.")
                self.profit += cost
                self.money_received = 0
                return True
            else:
                print("Sorry that's not enough money. Money refunded.")
                self.money_received = 0
                return False
