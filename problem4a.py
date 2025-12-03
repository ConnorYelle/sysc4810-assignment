from problem1c import get_permitted_operations, check_access
import user
import problem2c
def login_UI():
	logged_in = False
	username = input("Enter username: ").strip()
	password = input("Enter password: ").strip()
	validCredentials = problem2c.validate_user_password(username, password)
	if not validCredentials:
		print("Invalid username or password. Please try again.")
		return None
	else:
		logged_in = True
		print("Login successful!\n")

		logged_in_user = user.User(username, "Client", password)
		operations = get_permitted_operations(logged_in_user)
  
		print(f"Welcome, {username}! You are logged in as a {logged_in_user.get_role()}.")
		print("You have access to the following operations:")
		for operation in operations:
			print(f" - {operation}")
		while logged_in:
			selected_operation = input("\nSelect an operation to perform (or type 'logout' to log out): ").strip()
			if selected_operation.lower() == "logout":
				logged_in = False
				print("You have been logged out.\n")
			elif selected_operation in operations:
				print(f"Performing operation: {selected_operation}")
			else:
				print("You do not have access to that operation or it does not exist. Please try again.")
    
		

		