from abc import ABC, abstractmethod
from functools import wraps


def log_transaction(func):
    @wraps(func)
    def wrapper(self, amount):
        print(f"[LOG] Processing ₹{amount}")
        result = func(self, amount)
        print("[LOG] Transaction completed")
        return result
    return wrapper


class PaymentStrategy(ABC):

    @abstractmethod
    def validate(self):
        pass

    @abstractmethod
    def pay(self, amount):
        pass


class UPIPayment(PaymentStrategy):

    def __init__(self, upi_id):
        self.upi_id = upi_id

    def validate(self):
        return "@" in self.upi_id

    def pay(self, amount):
        if self.validate():
            return f"₹{amount} paid using UPI"
        return "Payment failed"


class CreditCardPayment(PaymentStrategy):

    def __init__(self, card_number):
        self.card_number = card_number

    def validate(self):
        return len(self.card_number) == 16

    def pay(self, amount):
        if self.validate():
            return f"₹{amount} paid using Credit Card"
        return "Payment failed"


class NetBankingPayment(PaymentStrategy):

    def __init__(self, bank):
        self.bank = bank

    def validate(self):
        return True

    def pay(self, amount):
        return f"₹{amount} paid using Net Banking ({self.bank})"


class PaymentProcessor:

    _registry = {}

    def __init__(self, strategy=None):
        self.strategy = strategy

    def set_strategy(self, strategy):
        self.strategy = strategy

    @log_transaction
    def process_payment(self, amount):
        return self.strategy.pay(amount)

    @classmethod
    def register_strategy(cls, name, strategy):
        cls._registry[name] = strategy

    @classmethod
    def create(cls, name, **kwargs):
        return cls(cls._registry[name](**kwargs))


# Register payment methods
PaymentProcessor.register_strategy("upi", UPIPayment)
PaymentProcessor.register_strategy("card", CreditCardPayment)
PaymentProcessor.register_strategy("netbanking", NetBankingPayment)

# UPI
processor = PaymentProcessor.create("upi", upi_id="user@bank")
print(processor.process_payment(1500))

# Switch to Credit Card
processor.set_strategy(CreditCardPayment("1234567890123456"))
print(processor.process_payment(2000))

# Switch to Net Banking
processor.set_strategy(NetBankingPayment("SBI"))
print(processor.process_payment(3000))