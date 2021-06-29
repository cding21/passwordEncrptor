from cryptography.fernet import Fernet


# def writekey():
#     key = Fernet.generate_key()
#     with open("key.key","wb") as key_file:
#         key_file.write(key)
#
# writekey()

def load_key():
    file = open("passwordEncryptor/key.key", "rb")
    key_tmp = file.read()
    file.close()
    return key_tmp


key = load_key()
fer = Fernet(key)


def view():
    with open("passwordEncryptor/passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.rstrip()
            acct, user_tmp, pw_tmp = data.split("|")
            print("Account: " + acct + "| Username :" + user_tmp + "| Password: " + fer.decrypt(pw_tmp.encode()).decode())


def add():
    acct = input("Associated account: ")
    name = input("New username: ")
    pw = input("New password: ")

    with open("passwordEncryptor/passwords.txt", "a") as f:
        f.write(acct + "|" + name + "|" + fer.encrypt(pw.encode()).decode() + "\n")


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
