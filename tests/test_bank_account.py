import os
import sys

import pytest

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
from src.bank_account import BankAccount

pytestmark = pytest.mark.bank


@pytest.fixture
def account():
    """An empty account owned by Alice."""
    return BankAccount("Alice")


@pytest.fixture
def funded_account(account):
    """Alice's account with 500.0 already deposited."""
    account.deposit(500.0)
    return account


@pytest.fixture
def bob():
    """A second, empty account."""
    return BankAccount("Bob")


# ----------------------------------------------------------------- deposit

@pytest.mark.parametrize("amount", [1, 100.0, 0.01, 999_999])
def test_deposit_increases_balance(account, amount):
    account.deposit(amount)
    assert account.get_balance() == amount


def test_deposit_records_transaction(account):
    account.deposit(25.0)
    assert account.get_transaction_count() == 1


@pytest.mark.xfail(reason="BUG #1: deposit accepts zero and negative amounts instead of raising ValueError", strict=True)
@pytest.mark.parametrize("bad_amount", [0, -1, -100.5])
@pytest.mark.edge
def test_deposit_invalid_amount_raises(account, bad_amount):
    with pytest.raises(ValueError):
        account.deposit(bad_amount)


# ---------------------------------------------------------------- withdraw

@pytest.mark.parametrize("amount, expected_balance", [
    (100.0, 400.0),
    (0.5, 499.5),
    (500.0, 0.0),
])
def test_withdraw_reduces_balance(funded_account, amount, expected_balance):
    funded_account.withdraw(amount)
    assert funded_account.get_balance() == expected_balance


@pytest.mark.edge
def test_withdraw_negative_raises(funded_account):
    with pytest.raises(ValueError):
        funded_account.withdraw(-10.0)


@pytest.mark.xfail(reason="BUG #2: withdraw permits overdrafts instead of raising ValueError", strict=True)
@pytest.mark.parametrize("amount", [501.0, 600.0, 1_000.0])
@pytest.mark.edge
def test_withdraw_overdraft_raises(funded_account, amount):
    with pytest.raises(ValueError):
        funded_account.withdraw(amount)


@pytest.mark.xfail(reason="BUG #2: failed overdraft withdrawal is not rejected and changes the balance", strict=True)
@pytest.mark.edge
def test_balance_unchanged_after_failed_withdraw(funded_account):
    with pytest.raises(ValueError):
        funded_account.withdraw(600.0)
    assert funded_account.get_balance() == 500.0


# ---------------------------------------------------------------- transfer

def test_transfer_reduces_sender_balance(funded_account, bob):
    funded_account.transfer(bob, 200.0)
    assert funded_account.get_balance() == 300.0


@pytest.mark.xfail(reason="BUG #3: transfer withdraws from the sender but never deposits into the receiver", strict=True)
def test_transfer_increases_receiver_balance(funded_account, bob):
    funded_account.transfer(bob, 200.0)
    assert bob.get_balance() == 200.0


# ------------------------------------------------------- owner and summary

def test_get_owner(account):
    assert account.get_owner() == "Alice"


def test_summary_contains_owner(account):
    assert "Alice" in account.get_summary()


@pytest.mark.xfail(reason="BUG #4: get_summary places Balance before Owner instead of starting with Owner:", strict=True)
def test_summary_starts_with_owner(account):
    assert account.get_summary().startswith("Owner:")


@pytest.mark.parametrize("amount", [10.0, 125.5, 999.0])
def test_summary_contains_balance(account, amount):
    account.deposit(amount)
    assert str(amount) in account.get_summary()
