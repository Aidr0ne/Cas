import json
import os
import time
import random
import link
from main import MISSIONS

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
				self.add(self.name)

		def add(self, name, link=""):
				while True:
						i = random.randint(1, 1000000)
						f = False
						for acc in self.data["numbers"]:
								if f == True:
										continue

								if acc["number"] == i:
										f = True
						if f == False:
								self.data["numbers"].append({"name": name, "number": i, "link": link})
								return i

		def load_data(self):
				try:
						with open(self.data_path, "r") as f:
								data = json.load(f)
				except FileNotFoundError:
						data = {"numbers": [{"name": "Bob", "number": 12345, "link": ""}, {"name": "???", "number": 1, "link": ""}]}

				return data

		def save_data(self):
				with open(self.data_path, "w") as f:
						json.dump(self.data, f)

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
						i = input("Y/N: ").lower()
						if i == "y":
								self.incoming_call()
								return
						else:
								pass

				print("Please Enter a phone number to try and call")
				i = int(input(": "))
				for acc in self.data["numbers"]:
						if acc["number"] == i:
								if acc["link"] == "":
										n = acc["name"]
										print(f"Looks like {n} Isn't Picking up")
										return
								else:
										a = "link." + acc["link"] + "()"
										eval(a)
										return

				input("Number Not Found...")

