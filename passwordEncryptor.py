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
    print("Account " + "| Username " + " | Password ")
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
            print(acct + " | " + user_tmp + " | " + fer.decrypt(pw_tmp.encode()).decode())
            counter += 1
    input("\n" + "Press enter to continue...")


def add():
    acct = input("Associated account: ")
    name = input("New username: ")
    pw = input("New password: ")

    with open("passwordEncryptor/passwords.txt", "a") as f:
        f.write(acct + "|" + name + "|" + fer.encrypt(pw.encode()).decode() + "\n")


# def writemaster():
#     master = input("Please input master password: ")
#     tmp = input("Please input master password again: ")
#     if master == tmp:
#         with open("passwordEncryptor/passwords.txt", "a") as f:
#             f.write(fer.encrypt(master.encode()).decode() + "\n")
#
# writemaster()

def check_key():
    pwcheck = input("Master password: ")
    with open("passwordEncryptor/passwords.txt", "r") as f:
        masterpw = fer.decrypt(f.readline().encode()).decode()
    if pwcheck == masterpw:
        return True
    else:
        print("Incorrect password, try again!")


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
