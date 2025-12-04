from problem2c import signup_new_password

def proactive_password_check(password: str) -> bool:
    
 	#check against common passwords
	common_passwords = open("common_passwds.txt", "r").read().splitlines()
	if password in common_passwords:
		print("Common password check failed, password is too common.")
		return False

	#check that the password meets the requirements defined in the assignment description
	#check length
	if len(password) < 8 or len(password) > 12:
		print("Length check failed, password must be between 8 and 12 characters.")
		return False
	
 	# allowed special characters
	specials = set("!@#$%*&")

	#check for special characters
	if not any(ch in specials for ch in password):
		print("Special character check failed, password must contain at least one special character (!@#$%*&).")
		return False

 	#check for uppercase letters
	if not any(char.isupper() for char in password):
		print("Uppercase letter check failed, password must contain at least one uppercase letter.")
		return False

	#check for digits
	if not any(char.isdigit() for char in password):
		print("Digit check failed, password must contain at least one digit.")
		return False

	return True

def signup_UI():

	username = input("Enter username: ").strip()
	print(
    "Make sure your password meets the following requirements:\n"
    " - Between 8 and 12 characters long\n"
    " - Cannot be the same as your username\n"
    " - Contains at least one uppercase letter\n"
    " - Contains at least one digit\n"
    " - Contains at least one special character from !@#$%*&\n"
    " - Is not a common password"
	)
	password = input("Enter password: ").strip()
	if username == password:
		print("Username and password cannot be the same. Please try again.")
		return
	elif proactive_password_check(password):
		signup_new_password(username, password, 300, "Client")
		print("Signup successful!")
		return
	else:
		print("Password does not meet the requirements. Please try again.")
		return
