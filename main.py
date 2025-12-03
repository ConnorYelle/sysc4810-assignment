from problem3b import signup_UI

if __name__ == "__main__":
	running = True
	logged_in = False
	user = None
	print("------- Welcome to the JustInvest System -------")
 
	while running:	
		action = input("\nSelect an action: sign-up, login, quit: ").strip().lower()
		if action == "sign-up":
			signup_UI()
		elif action == "login":
			#login_UI()
			print("Login functionality not yet implemented.\n")
		elif action == "quit":
			print("Exiting the JustInvest System.\n")
			running = False
		else:
			print("Invalid entry. Please try again.\n")
