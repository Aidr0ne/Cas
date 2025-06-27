def J1():
    print("Hello Welcome to the StoreMart custumor helpline how can we help today?")
    print("1. Job")
    print("2. Contact a member of staff")
    print("3. Goodbye")
    i = input("1-3: ")
    from main import PHONE
    if i == "1":
        print("Sorry we are not looking for any crew members right now")
    elif i == "2":
        print("Sorry Our agent is currently not on shift please call him through this number")
        i = PHONE.add("StoreMartAgent", "SMA")
        print(i)

def SMA():
    print("SMA")