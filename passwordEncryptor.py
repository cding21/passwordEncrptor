from cryptography.fernet import Fernet
import math


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


def header_centre(word, number):
    return "-" * math.ceil((number - len(word) + 4) / 2) + word + "-" * math.ceil((number - len(word) + 4) / 2)


def centre(word, number):
    return " " * math.ceil((number - len(word) + 4) / 2) + word + " " * math.ceil((number - len(word) + 4) / 2)


def view():
    maxAcc = ""
    maxUser = ""
    maxPw = ""
    counter = 1
    with open("passwordEncryptor/passwords.txt", "r") as f:
        for line in f.readlines():
            if counter == 1:
                counter += 1
                continue
            elif line == "":
                break
            data = line.rstrip()
            acct, user_tmp, pw_tmp = data.split("|")
            if len(acct) > len(maxAcc):
                maxAcc = acct
            if len(user_tmp) > len(maxUser):
                maxUser = user_tmp
            if len(fer.decrypt(pw_tmp.encode()).decode()) > len(maxPw):
                maxPw = fer.decrypt(pw_tmp.encode()).decode()

    print(header_centre("Account", len(maxAcc)) + "|" + header_centre("Username", len(maxUser)) + "|" + header_centre(
        "Password", len(maxPw)))

    counter = 1
    with open("passwordEncryptor/passwords.txt", "r") as f:
        for line in f.readlines():
            if counter == 1:
                counter += 1
                continue
            elif line == "":
                break
            data = line.rstrip()
            acct, user_tmp, pw_tmp = data.split("|")

            print(centre(acct, len(maxAcc)) + "|" + centre(user_tmp, len(maxUser)) + "|"
                  + centre(fer.decrypt(pw_tmp.encode()).decode(), len(maxPw)))

    input("\n" + "Press enter to continue...")


def add():
    acct = input("Associated account: ")
    name = input("New username: ")
    pw = input("New password: ")

    with open("passwordEncryptor/passwords.txt", "a") as f:
        f.write(acct + "|" + name + "|" + fer.encrypt(pw.encode()).decode() + "\n")


def writemaster():
    master = input("Please input master password: ")
    tmp = input("Please input master password again: ")
    if master == tmp:
        with open("passwordEncryptor/passwords.txt", "a") as f:
            f.write(fer.encrypt(master.encode()).decode() + "\n")


def check_key():
    with open("passwordEncryptor/passwords.txt", "r") as f:
        tmp = f.readline()
        if tmp == "":
            writemaster()
    with open("passwordEncryptor/passwords.txt", "r") as f:
        masterpw = fer.decrypt(f.readline().encode()).decode()
    pwcheck = input("Master password: ")
    if pwcheck == masterpw:
        return True
    else:
        print("Incorrect password, try again!")
        check_key()


pw = check_key()

while pw:
    mode = input("\nChoose from the following options: \n1 : View current passwords\n2 : Add a new password\n\nPress q "
                 "to quit\n")
    if mode == "q":
        break
    if mode == "1":
        view()
    elif mode == "2":
        add()
    else:
        print("Invalid input, please select from the list of options!")
