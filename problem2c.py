import hashlib
import os

def signup_new_password(username, password, iterations: int):
    #16 bytes because it is large enough to guarantee uniqueness across users
    salt = os.urandom(16)

    #hash the password for 100 iterations using sha-256
    hashed = hashlib.pbkdf2_hmac('sha256', password.encode('utf-8'), salt, iterations)
    hex_hashed = hashed.hex()
    hex_salt = salt.hex()
    
    try:
        with open("passwd.txt", "w") as file:
            file.write(username+","+hex_hashed+","+hex_salt+","+str(iterations))
    except FileNotFoundError:
        print("Password file not found...")

    file.close()

if __name__ == "__main__":
    signup_new_password("Connor", "123password1", 300)





    