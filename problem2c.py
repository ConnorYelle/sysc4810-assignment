import hashlib
import os

def signup_new_password(username, password, iterations: int, role: str) -> bool:

    #16 bytes because it is large enough to guarantee uniqueness across users
    salt = os.urandom(16)

    #hash the password for the given number of iterations using sha-256
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    hex_hashed = hashed.hex()
    hex_salt = salt.hex()

    #check if the username already exists in the password file
    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                line = line.strip()
                if not line:
                    continue
                stored_data = line.split(",")
                stored_username = stored_data[0]
                if stored_username == username:
                    print("Username already exists...")
                    return False
    except FileNotFoundError:
        print("Password file not found")
        return False

    #append the new user to the password file
    try:
        with open("passwd.txt", "a") as file:
            file.write(username + "," + hex_hashed + "," + hex_salt + "," + str(iterations) + ","+role+ "\n")
        return True
    except FileNotFoundError:
        print("Password file not found...")
        return False


def validate_user_password(username, password) -> bool:
    try:
        with open("passwd.txt", "r") as file:
            for line in file:
                stored_data = line.strip().split(",")
                stored_username = stored_data[0]
                stored_hashed_password = stored_data[1]
                stored_salt = bytes.fromhex(stored_data[2])
                stored_iterations = int(stored_data[3])

                if username != stored_username:
                    continue

                #hash the provided password with the stored salt and iterations
                hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), stored_salt, stored_iterations)
                hex_hashed = hashed.hex()

                if hex_hashed == stored_hashed_password:
                    return True
                else:
                    return False
                
    except FileNotFoundError:
        print("Password file not found...")
        return False
    
    file.close()
    return False



    

    