from unittest.mock import patch, mock_open
import hashlib
import problem2c

tests_passed = 0
tests_failed = 0

def test_validate_user_password():
	global tests_passed, tests_failed
	username = "testuser"
	correct_password = "Test@1234"
	wrong_password = "WrongPass1!"

	#mock a fake password file
	salt = b"1234567890123456" #16 bytes salt
	iterations = 1000
	hashed = hashlib.pbkdf2_hmac('sha256', correct_password.encode('utf-8'), salt, iterations)
	stored_data = f"{username},{hashed.hex()},{salt.hex()},{iterations}\n"

	try:
     #again patch the open() function to use the fake password file
		with patch("builtins.open", mock_open(read_data=stored_data)):
			result = problem2c.validate_user_password(username, correct_password)
			assert result == True
			print("Correct password validation tests passed.")
			tests_passed += 1
	except AssertionError:
		print("Correct password validation tests failed.")
		tests_failed += 1
	except Exception as e:
		print(f"Correct password validation tests error: {e}")
		tests_failed += 1

	try:
		with patch("builtins.open", mock_open(read_data=stored_data)):
			result = problem2c.validate_user_password(username, wrong_password)
			assert result == False
			print("Wrong password validation tests passed.")
			tests_passed += 1
	except AssertionError:
		print("Wrong password validation tests failed.")
		tests_failed += 1
	except Exception as e:
		print(f"Wrong password validation tests error: {e}")
		tests_failed += 1

if __name__ == "__main__":
    print("\n------------- Password File Tests -------------")
    test_validate_user_password()
    print(f"\nPassword File Tests Passed: {tests_passed}")
    print(f"Password File Tests Failed: {tests_failed}\n")
