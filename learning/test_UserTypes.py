

from UserTypes import BankAccount, Gender
from UserTypes import Person

def test_bank_account_transfer():
    acc1 = BankAccount("ID1", Person("sai", 44, Gender.M), 1000, "privilised")
    acc2 = BankAccount("ID2", Person("neerja", 39, Gender.F), 2000, "non privilised")

    acc1.transfer_to(acc2, 500)

    assert acc1.balance == 500

    acc1.transfer_to( acc2, 500)

    assert acc1.balance == 0

    acc2.transfer_to( acc1, 2500)

    assert acc2.balance == 500

    acc2.transfer_to( acc1, 500)

    assert acc2.balance == 500

    acc3 = BankAccount("ID3", Person("Padmaja", 39, Gender.F), 2000, "overdraft")

    acc3.transfer_to( acc1, 3000 )

    assert acc3.balance == -1000

    acc3.transfer_to(acc2, 1000 )

    assert acc3.balance == -2000