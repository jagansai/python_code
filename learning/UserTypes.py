# Let's create a type called Person.
# Person will have name, age, gender


from enum import Enum
from traceback import print_last

class Gender(Enum):
    M = "Male"
    F = "Female"

class Person:
    def __init__(self, name, age: int, gender : Gender):
        self.name = name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f"Name: {self.name } \nAge: {self.age} \nGender:{self.gender.value}"

class Grade:
    def __init__(self, name: str):
        self.name = name

    def __str__(self):
        return f"{self.name}"

class School:
    def __init__(self, name,grade: Grade):
        self.name = name
        self.grade = grade

    def __str__(self):
        return f"School:{self.name},{self.grade}"


class Student(Person):
    def __init__(self, name, age, gender: Gender, school : School):
        super().__init__(name, age, gender)
        self.school = school

    def __str__(self):
        return f"{super().__str__()}\n{self.school}"


class BankAccount:
    def __init__(self, id,person:Person,balance:int):
        self.id = id
        self.person = person
        self.balance = balance

    def __str__(self):
        return f"Account:{self.id}\n{self.person}\nBalance:{self.balance}"

    def transfer_to(self, otherAccount, amount: int):
        if self.balance - amount<500:
           print("insufficient balance")
        else:
           self.balance = self.balance - amount
           otherAccount.balance = otherAccount.balance + amount


# Create 2 bank accounts
# One with balance of 2000
# Another with balance of 5000
# Print both the accounts
# Now transfer 1000 from Account1 to Account2.

# 02-Jul-2023
# Add a new field to BankAccount that indicates if the account is privileged or non-privileged
# if it is a privileged account, there is no requirement to maintain minimum balance.
# if it is a non-privileged account, the account needs to maintain minimum balance.




sai = Person("Sai", 44, Gender.M)
neeraja = Person("neeraja", 39, Gender.F)
karthik = Student("Karthik", 11, Gender.M, School("DPS", Grade("6C")))



print(sai)
#print(type(sai))

print(neeraja)
print(karthik)

#creating bank account

id1= BankAccount("A1",Person("Aadi",22,Gender.M),2000)

id2 = BankAccount("A2",Person("Sudha",21,Gender.F),3000)

print(id1)
print(id2)

#Transfer money from id2 to id1
print("transfering money from id2 ti id1")
id2.transfer_to(id1,1000)
print(id1)
print(id2)

id2.transfer_to(id1,3000)

print(id1)
print(id2)

