
from unittest.mock import patch, mock_open
import problem2c
import problem3b

signup_tests_passed = 0
signup_tests_failed = 0
password_check_tests_passed = 0
password_check_tests_failed = 0

def test_signup():
    global signup_tests_passed, signup_tests_failed
    username = "testuser"
    passwordValid = "Test@1234"
    passwordSameUser = "testuser"

    try:
        #mock an empty file so we don't interfere with actual passwd.txt
        with patch("builtins.open", mock_open(read_data="")):
            result = problem2c.signup_new_password(username, passwordValid, 1000, "Client")
            assert result == True
            print("New user signup tests passed.")
            signup_tests_passed += 1
    except AssertionError:
        print("New user signup tests failed.")
        signup_tests_failed += 1
    except Exception as e:
        print(f"New user signup tests error: {e}")
        signup_tests_failed += 1

    try:
        #mock a fake password file that does not interfere with actual passwd.txt
        existing_data = f"{username},hash,salt,1000\n"
         #builtins.open means that we patch the open() function to use our mock instead of the real one
        with patch("builtins.open", mock_open(read_data=existing_data)): 
            result = problem2c.signup_new_password(username, passwordSameUser, 1000, "Client")
            assert result == False
            print("Same username signup tests passed.")
            signup_tests_passed += 1
    except AssertionError:
        print("Same username signup tests failed.")
        signup_tests_failed += 1
    except Exception as e:
        print(f"Same username signup tests error: {e}")
        signup_tests_failed += 1
        
def proactive_password_check_test():
    global password_check_tests_passed, password_check_tests_failed

    #test passwords for different failures
    passwordNoSpecial = "Test1234"
    passwordNoUpper = "test@1234"
    passwordNoDigit = "Test@abcd"
    passwordTooShort = "T@1a"
    passwordTooLong = "Test@12345678"
    passwordCommon = "password"
    passwordValid = "Test@1234"

    #no special character
    try:
        assert problem3b.proactive_password_check(passwordNoSpecial) == False
        print("No special character test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("No special character test failed.")
        password_check_tests_failed += 1

    #no uppercase letter
    try:
        assert problem3b.proactive_password_check(passwordNoUpper) == False
        print("No uppercase letter test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("No uppercase letter test failed.")
        password_check_tests_failed += 1

    #no digit
    try:
        assert problem3b.proactive_password_check(passwordNoDigit) == False
        print("No digit test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("No digit test failed.")
        password_check_tests_failed += 1

    #too short
    try:
        assert problem3b.proactive_password_check(passwordTooShort) == False
        print("Too short password test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("Too short password test failed.")
        password_check_tests_failed += 1

    #too long
    try:
        assert problem3b.proactive_password_check(passwordTooLong) == False
        print("Too long password test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("Too long password test failed.")
        password_check_tests_failed += 1

    #common password
    try:
        assert problem3b.proactive_password_check(passwordCommon) == False
        print("Common password test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("Common password test failed.")
        password_check_tests_failed += 1

    #valid password
    try:
        assert problem3b.proactive_password_check(passwordValid) == True
        print("Valid password test passed.")
        password_check_tests_passed += 1
    except AssertionError:
        print("Valid password test failed.")
        password_check_tests_failed += 1


if __name__ == "__main__":
	print("\n------------- Signup Tests -------------")
	test_signup()
	print(f"\nSignup Tests Passed: {signup_tests_passed}")
	print(f"Signup Tests Failed: {signup_tests_failed}\n")
 
	print("\n------------- Proactive Password Tests -------------")
	proactive_password_check_test()
	print(f"\nPassword Check Tests Passed: {password_check_tests_passed}")
	print(f"Password Check Tests Failed: {password_check_tests_failed}\n")