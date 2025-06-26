import json
import os
import time

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
								print


class Player:
		def __init__(self):
				self.cash = 0
				self.mission = 1
				self.mission_start = 0
				self.name = str(input("Please Enter Your Name: "))
				self.location = "Street"

class Bank:
		def __init__(self):
				self.data_path = "data/bank.json"
				self.data = self.load_data()

		def load_data(self):
				try:
						with open(self.data_path, "r") as f:
								data = json.load(f)
				except FileNotFoundError:
						data = {"accounts": [{"name": "bob", "balance": 100, "vip": ""}]}

				return data

		def save_data(self):
				with open(self.data_path, "w") as f:
						json.dump(self.data, f)

		def check_account(self, name):
				for acc in self.data["accounts"]:
						if acc["name"] == name:
								print("Name: ", acc["name"])
								print("Balance", acc["balance"])
								print(acc["vip"])
								input("...")
								return

				input("Account Not found...")

		def make_account(self, name):
				for acc in self.data["accounts"]:
						if acc["name"] == name:
								input("You allready have an account: ")
								return
				self.data["accounts"].append({"name": name, "balance": 0, "vip": ""})

		def deposit(self, name, amount):
				for acc in self.data["accounts"]:
						if acc["name"] == name:
								acc["balance"] += amount
								input("Deposited Money...")
				input("Account not found...")

		def balance(self, name):
				for acc in self.data["accounts"]:
						if acc["name"] == name:
								return acc["balance"]
				return 0

		def withdraw(self, name, amount):
				for acc in self.data["accounts"]:
						if acc["name"] == name:
								acc["balance"] -= amount
								input("Withdrawing Money...")
				input("Account not found...")

class Missions:
		def __init__(self):
				self.data_path = "data/missions.json"
				self.data = self.load_data()

		def load_data(self):
				with open(self.data_path, "r") as f:
						data = json.load(f)

				return data

		def check(self):
				global phone_ringing, caller

				if PLAYER.mission == 1:
						if PLAYER.mission_start == 0:
								phone_ringing = True
								caller = self.data["1"]["number"]
						else:
								pass

		def get_dialogue(self, mission):
				return self.data[str(mission)]["sd"]

		def start(self, number):
				global phone_ringing, ringer
				PLAYER.mission_start = 1
				phone_ringing = False
				ringer = 0


class Phone:
		def __init__(self, name):
				self.name = name
				self.data_path = "data/phone.json"
				self.data = self.load_data()
				self.register_name(self.name)

		def register_name(self, name):
				# TODO: ADD PLAYER TO THE LIST
				pass

		def load_data(self):
				try:
						with open(self.data_path, "r") as f:
								data = json.load(f)
				except FileNotFoundError:
						data = {"numbers": [{"name": "Bob", "number": 12345}, {"name": "???", "number": 1}], "ava": []}

				for i in range(1, 1000000):
						for n in data["numbers"]:
								if i == n["number"]:
										continue
						data["ava"].append(i)

				return data

		def incoming_call(self):
				if caller == 1: # Quest Giver
						if PLAYER.mission_start == 0:
								talk(MISSIONS.get_dialogue(PLAYER.mission))
								MISSIONS.start(PLAYER.mission)
				else:
						pass
				input("...")

		def handle(self):
				if phone_ringing:
						print("The phone is ringing Do You want to answer?")
						i = input("Y/N").lower()
						if i == "y":
								self.incoming_call()



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
				PHONE.handle()


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
				print("10: Inspect the Bank")
		i = int(input("1 - 9: "))

		if i == 1:
				BANK.check_account(PLAYER.name)
		elif i == 2:
				BANK.make_account(PLAYER.name)
				input("Sucsess...")
		elif i == 3:
				i = int(input("Please enter amount to deposit: "))
				if i > PLAYER.cash:
						input("You dont have enough cash...")
						return
				else:
						PLAYER.cash -= i
						BANK.deposit(PLAYER.name, i)
		elif i == 4:
				i = int(input("Please enter amount to withdraw: "))
				if i > BANK.balance(PLAYER.name):
						input("Thats more cash than you have")
						return
				else:
						PLAYER.cash += i
						BANK.withdraw(PLAYER.name, i)
		elif i == 5:
				pass
		elif i == 6:
				pass
		elif i == 7:
				pass
		elif i == 8:
				pass
		elif i == 9:
				PLAYER.location = "Street"
		elif i == 10: # Mission 1
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


places = {
		"Home": home,
		"Bank": bank,
		"Street": street,
}

# Constants
print("Do you want swearing in your runthrough")
print("1. Not a chance mate")
print("2. ****")
print("3. idc")
CLEAN = int(input("1 - 3"))

talk("Fuck lets go")

# Global Variables
global phone_ringing, caller
phone_ringing = True
caller = 1

# Objects
PLAYER = Player()
BANK = Bank()
MISSIONS = Missions()
PHONE = Phone(PLAYER.name)

while True:
		os.system("clear")
		places[PLAYER.location]()
		save()