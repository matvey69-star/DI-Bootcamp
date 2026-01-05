#Exercise 1: Currencies
class Currency:
    def __init__(self, currency, amount):
        self.currency = currency
        self.amount = amount

    # ---------- Dunder Methods ----------

    def __str__(self):
        # User-friendly string
        return f"{self.amount} {self.currency}s"

    def __repr__(self):
        # Developer-friendly representation
        return f"{self.amount} {self.currency}s"

    def __int__(self):
        return self.amount

    def __add__(self, other):
        if isinstance(other, int):
            return self.amount + other

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            return self.amount + other.amount

        raise TypeError("Unsupported type for addition")

    def __iadd__(self, other):
        if isinstance(other, int):
            self.amount += other
            return self

        if isinstance(other, Currency):
            if self.currency != other.currency:
                raise TypeError(
                    f"Cannot add between Currency type <{self.currency}> and <{other.currency}>"
                )
            self.amount += other.amount
            return self

        raise TypeError("Unsupported type for addition")
c1 = Currency('dollar', 5)
c2 = Currency('dollar', 10)
c3 = Currency('shekel', 1)
c4 = Currency('shekel', 10)

print(c1)
print(int(c1))
print(repr(c1))
print(c1 + 5)
print(c1 + c2)

c1 += 5
print(c1)

c1 += c2
print(c1)
#print(c1 + c3)  # This will raise a TypeError

#Exercise 3: String module
import string
import random
letters = string.ascii_letters
random_string = ""

for _ in range(5):
    random_char = random.choice(letters)
    random_string += random_char

print(random_string)
#Exercise 4: Current Date
import datetime

def display_current_date():
    today = datetime.date.today()
    formatted_date = today.strftime("%d/%m/%Y")
    print(formatted_date)

display_current_date()

#Exercise 5: Amount of time left until January 1st
import datetime

def time_until_new_year():
    now = datetime.datetime.now()
    january_first = datetime.datetime(now.year + 1, 1, 1)
    time_left = january_first - now

    days = time_left.days
    hours, remainder = divmod(time_left.seconds, 3600)
    minutes, seconds = divmod(remainder, 60)

    print(
        f"Time left until January 1st: "
        f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds"
    )

time_until_new_year()

#Exercise 6: Birthday and minutes
import datetime
def minutes_lived(birthdate_str):
    # Step 1: convert string to datetime
    birthdate = datetime.datetime.strptime(birthdate_str, "%d/%m/%Y")

    # Step 2: get current date and time
    now = datetime.datetime.now()

    # Step 3: calculate time difference
    time_difference = now - birthdate

    # Step 4: convert seconds to minutes
    minutes = int(time_difference.total_seconds() / 60)

    print(f"You have lived approximately {minutes:,} minutes.")
minutes_lived("08/07/1980")

#Exercise 7: Faker Module
from faker import Faker
fake = Faker()
users = []

def generate_users(num_users):
    for _ in range(num_users):
        user = {
            "name": fake.name(),
            "address": fake.address(),
            "language_code": fake.language_code()
        }
        users.append(user)

generate_users(5)

for user in users:
    print(user)