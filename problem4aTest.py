from unittest.mock import patch
import problem4a 

tests_passed = 0
tests_failed = 0

from unittest.mock import patch, mock_open
import problem4a

tests_passed = 0
tests_failed = 0

def login_ui_test():
    global tests_passed, tests_failed

    #mock passwd.txt content: username,hash,salt,iterations,role
    passwd_data = "testuser,hash,salt,1000,Client\n"

    with patch("builtins.input", side_effect=["testuser", "Test@1234", "logout"]), \
         patch("problem2c.validate_user_password", return_value=True), \
         patch("builtins.open", mock_open(read_data=passwd_data)), \
         patch("builtins.print") as mock_print:

        problem4a.login_UI()
        printed = " ".join(str(call.args[0]) for call in mock_print.call_args_list)

    #login success message
    try:
        assert "Login successful!" in printed
        print("Login success message test passed.")
        tests_passed += 1
    except AssertionError:
        print("Login success message test failed.")
        tests_failed += 1

    #logout message
    try:
        assert "You have been logged out." in printed
        print("Logout message test passed.")
        tests_passed += 1
    except AssertionError:
        print("Logout message test failed.")
        tests_failed += 1

    #welcome message with role
    try:
        assert "Welcome, testuser! You are logged in as a Client." in printed
        print("Welcome message and role test passed.")
        tests_passed += 1
    except AssertionError:
        print("Welcome message and role test failed.")
        tests_failed += 1

    #operations header
    try:
        assert "You have access to the following operations:" in printed
        print("Operations header test passed.")
        tests_passed += 1
    except AssertionError:
        print("Operations header test failed.")
        tests_failed += 1

    #allowed operation
    try:
        assert " - view_account_balance" in printed
        print("Allowed operation test passed.")
        tests_passed += 1
    except AssertionError:
        print("Allowed operation test failed.")
        tests_failed += 1

    #forbidden operation
    try:
        assert " - modify_investment_portfolio" not in printed
        print("Forbidden operation test passed.")
        tests_passed += 1
    except AssertionError:
        print("Forbidden operation test failed.")
        tests_failed += 1

if __name__ == "__main__":
    print("\n------------- Login UI Tests -------------")
    login_ui_test()
    print(f"\nLogin UI Tests Passed: {tests_passed}")
    print(f"Login UI Tests Failed: {tests_failed}\n")

