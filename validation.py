import re
from datetime import datetime, time
from tkinter import ttk

def name_validator(name):
    if type(name) == str and re.match(r"^[a-zA-Z\s]{3,30}$", name):
        return name
    else:
        raise ValueError("Invalid name !!!")


def pay_type_validator(pay_type):
    pay_type = pay_type.get()
    print("your pay type is : ", pay_type)


# 	def option_selected(event):
#    selected_option = combo.get()
#    print("You selected:", selected_option)


def amount_validator(amount):
    try:
        if type(amount) == int and amount > 0:
            return amount
    except:
        raise ValueError("Invalid amount !!!")


def time_validator(doc_time):
    try:
        if type(doc_time) == datetime:
            return datetime.strptime(doc_time, "%H:%M ").time()
    except Exception as e:
        raise ValueError("Invalid Time !!!", f"error: {e}")


def date_validator(doc_date):
    try:
        if type(doc_date) == str:
            return datetime.strptime(doc_date, "%Y-%m-%d").date()
    except Exception as e:
        raise ValueError("Invalid Date !!!", f"error: {e}")


def price_validation(price):
    if price > 0:
        return True
    else:
        return False


def pay_type_validation(pay_type):
    return pay_type in ["cash", "card", "check"]


def year_validator(year):
    if 1910 <= year <= 2025:
        return True
    else:
        print("Invalid Year !!!")
        return False


def age_validator(age):
    return 0 < age < 150
