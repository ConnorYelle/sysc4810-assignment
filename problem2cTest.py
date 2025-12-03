import problem2c

tests_passed = 0
tests_failed = 0

def test_signup():
	global tests_passed, tests_failed
	username = "testuser"
	passwordValid = "Test@1234"
	passwordSameUser = "testuser"  # same as username
	
	# Attempt to sign up the new user
	result1 = problem2c.signup_new_password(username, passwordValid, 1000)
	result2 = problem2c.signup_new_password(username, passwordSameUser, 1000)
	
	try:
		assert result1 == True
		assert result2 == False
	except AssertionError:
		print("Signup test failed.")
		tests_failed += 1
		return
	
	print("Signup test passed.")
	tests_passed += 1