"""
BankAccount — intentional bugs hidden inside. Find them with tests!
"""


class BankAccount:
    """A simple bank account with deposit, withdraw, transfer, and summary."""

    def __init__(self, owner: str):
        self.owner = owner
        self._balance = 0.0
        self._transactions = []

    def deposit(self, amount: float) -> None:
        """
        Deposit amount into account.
        Should raise ValueError if amount <= 0.
        """
        self._balance += amount
        self._transactions.append(("deposit", amount))

    def withdraw(self, amount: float) -> None:
        """
        Withdraw amount from account.
        Should raise ValueError if amount > balance (overdraft not allowed).
        """
        if amount < 0:
            raise ValueError("Amount must be positive")
        self._balance -= amount
        self._transactions.append(("withdraw", amount))

    def transfer(self, target: "BankAccount", amount: float) -> None:
        """
        Transfer amount from this account to target.
        Should reduce this balance AND increase target balance.
        """
        self.withdraw(amount)

    def get_balance(self) -> float:
        return self._balance

    def get_owner(self) -> str:
        return self.owner

    def get_transaction_count(self) -> int:
        return len(self._transactions)

    def get_summary(self) -> str:
        """
        Returns summary string: "Owner: X | Balance: Y | Transactions: Z"
        """
        return f"Balance: {self._balance} | Owner: {self.owner} | Transactions: {len(self._transactions)}"
