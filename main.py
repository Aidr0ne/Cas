import json
import os
import time
import random
import objects as o
import link

swears = ["fuck", "shit", "bitch", "cunt"]

def talk(say):
    for word in say.split(" "):
        if word in swears:
            if CLEAN == 1:
                pass
            elif CLEAN == 2:
                a = ""
                for letter in word:
                    a += "*"
                print(a, end=" ")
            else:
                print(word, end=" ")
        else:
          print(word, end=" ")

    print("\n")


        



def home():
    if phone_ringing:
        print("The Phone's Ringing")
    print("What do you want like to do: ")
    print("1. Go to sleep")
    print("2. Go onto the street")
    print("3. Use the phone")
    i = int(input("1 - 3: "))
    if i == 1:
        pass
    elif i == 2:
        PLAYER.location = "Street"
    elif i == 3:
        PHONE.handle(MISSIONS, PLAYER)


def bank():
    print("What would you like to do: ")
    print("1. Check Account")
    print("2. Create New Account")
    print("3. Deposit Money")
    print("4. Withdraw Money")
    print("5. List Debts")
    print("6. Pay Debts")
    print("7. View Top Accounts")
    print("8. Go Up The Lift")
    print("9. Leave")

    if PLAYER.mission == 1 and PLAYER.mission_start == 1:
        print("M1: Inspect the Bank")
    i = input("1 - 9: ")

    if i == "1":
        BANK.check_account(PLAYER.name)
    elif i == "2":
        BANK.make_account(PLAYER.name)
        input("Sucsess...")
    elif i == "3":
        i = int(input("Please enter amount to deposit: "))
        if i > PLAYER.cash:
            input("You dont have enough cash...")
            return
        else:
            PLAYER.cash -= i
            BANK.deposit(PLAYER.name, i)
    elif i == "4":
        i = int(input("Please enter amount to withdraw: "))
        if i > BANK.balance(PLAYER.name):
            input("Thats more cash than you have")
            return
        else:
            PLAYER.cash += i
            BANK.withdraw(PLAYER.name, i)
    elif i == "5":
        pass
    elif i == "6":
        pass
    elif i == "7":
        pass
    elif i == "8":
        pass
    elif i == "9":
        PLAYER.location = "Street"
    elif i == "M1": # Mission 1
        pass


def street():
    print("What would you like to do: ")
    print("1. Go to the Bank")
    print("2. Go Home")

    i = int(input("1 - 2: "))
    if i == 1:
        PLAYER.location = "Bank"
    elif i == 2:
        PLAYER.location = "Home"

def save():
    BANK.save_data()
    PHONE.save_data()

def store():
    pass

def market():
    pass

def casino():
    pass

places = {
    "Home": home,
    "Bank": bank,
    "Street": street,
    "Store": store,
    "Market": market,
    "Casino": casino
}

# Constants
print("Do you want swearing in your runthrough")
print("1. Not a chance mate")
print("2. ****")
print("3. idc")

global CLEAN

CLEAN = int(input("1 - 3: "))

talk("fuck lets go")

# Global Variables
global phone_ringing, caller, ringer
phone_ringing = True
caller = 1
ringer = 0

# Objects
global PLAYER, BANK, MISSIONS, PHONE
PLAYER = o.Player()
BANK = o.Bank()
MISSIONS = o.Missions()
PHONE = o.Phone(PLAYER.name)

while True:
    os.system("clear")
    MISSIONS.check(PLAYER)
    places[PLAYER.location]()
    save()