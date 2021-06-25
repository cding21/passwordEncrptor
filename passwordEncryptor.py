masterpw = input("Master password: ")

def view():
    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            acct, userTmp, pwTmp = data.split("|")
            print("Account: " + acct + "| Username :" + userTmp + "| Password: " + pwTmp)

def add():
    acct = input("Associated account: ")
    name = input("New username: ")
    pw = input("New password: ")

    with open("passwords.txt","a") as f:
        f.write(acct + "|" + name + "|" + pw + "\n")

def encrypt(str):
    pass

def decrypt(str):
    pass


while True:
    mode = input("Choose from the following options: \n1 : View current password\n2 : Add a new password\n")
    if mode == "q":
        break
    if mode == "1":
        view()
    elif mode == "2":
        add()
    else:
        print("Invalid input, please select from the list of options!")
