import RBAC
import user

tests_passed = 0
tests_failed = 0

def test_rbac_client():
	global tests_passed, tests_failed
	userClient = user.User("alice", "Client", "hriwaogot47fjnfkafbn") #password does not matter for RBAC
	clientOperations = RBAC.get_permitted_operations(userClient)
	# Try all the assertions and if a failure is present, catch it and print a fail message
	try:
		assert userClient.get_role() == "Client"
		assert "view_account_balance" in clientOperations
		assert "view_investment_portfolio" in clientOperations
		assert "modify_investment_portfolio" not in clientOperations
		assert "view_financial_adivisor_contact" in clientOperations
		assert "view_financial_planner_contact" not in clientOperations
		assert "view_money_market_instruments" not in clientOperations
		assert "view_private_consumer_instruments" not in clientOperations
	except AssertionError:
		print("Client RBAC tests failed.")
		tests_failed += 1
		return
	print("Client RBAC tests passed.")
	tests_passed += 1

def test_rbac_premium_client():
	global tests_passed, tests_failed
	userPremiumClient = user.User("alice", "Premium Client", "hriwaogot47fjnfkafbn")
	premiumClientOperations = RBAC.get_permitted_operations(userPremiumClient)
	try:
		assert userPremiumClient.get_role() == "Premium Client"
		assert "view_account_balance" in premiumClientOperations
		assert "view_investment_portfolio" in premiumClientOperations
		assert "modify_investment_portfolio" in premiumClientOperations
		assert "view_financial_adivisor_contact" in premiumClientOperations
		assert "view_financial_planner_contact" in premiumClientOperations
		assert "view_money_market_instruments" not in premiumClientOperations
		assert "view_private_consumer_instruments" not in premiumClientOperations
	except AssertionError:
		print("Premium Client RBAC tests failed.")
		tests_failed += 1
		return
	print("Premium Client RBAC tests passed.")
	tests_passed += 1

def test_rbac_financial_advisor():
	global tests_passed, tests_failed
	userFinancialAdvisor = user.User("alice", "Financial Advisor", "hriwaogot47fjnfkafbn")
	financialAdvisorOperations = RBAC.get_permitted_operations(userFinancialAdvisor)
	try:
		assert userFinancialAdvisor.get_role() == "Financial Advisor"
		assert "view_account_balance" in financialAdvisorOperations
		assert "view_investment_portfolio" in financialAdvisorOperations
		assert "modify_investment_portfolio" in financialAdvisorOperations
		assert "view_financial_adivisor_contact" not in financialAdvisorOperations
		assert "view_financial_planner_contact" not in financialAdvisorOperations
		assert "view_money_market_instruments" not in financialAdvisorOperations
		assert "view_private_consumer_instruments" in financialAdvisorOperations
	except AssertionError:
		print("Financial Advisor RBAC tests failed.")
		tests_failed += 1
		return
	print("Financial Advisor RBAC tests passed.")
	tests_passed += 1

def test_rbac_financial_planner():
	global tests_passed, tests_failed
	userFinancialPlanner = user.User("alice", "Financial Planner", "hriwaogot47fjnfkafbn")
	financialPlannerOperations = RBAC.get_permitted_operations(userFinancialPlanner)
	try:
		assert userFinancialPlanner.get_role() == "Financial Planner"
		assert "view_account_balance" in financialPlannerOperations
		assert "view_investment_portfolio" in financialPlannerOperations
		assert "modify_investment_portfolio" in financialPlannerOperations
		assert "view_financial_adivisor_contact" not in financialPlannerOperations
		assert "view_financial_planner_contact" not in financialPlannerOperations
		assert "view_money_market_instruments" in financialPlannerOperations
		assert "view_private_consumer_instruments" in financialPlannerOperations
	except AssertionError:
		print("Financial Planner RBAC tests failed.")
		tests_failed += 1
		return
	print("Financial Planner RBAC tests passed.")
	tests_passed += 1

def test_rbac_teller():
	global tests_passed, tests_failed
	userTeller = user.User("alice", "Teller", "hriwaogot47fjnfkafbn")
	tellerOperations = RBAC.get_permitted_operations(userTeller)
	try:
		assert userTeller.get_role() == "Teller"
		assert "view_account_balance" in tellerOperations
		assert "view_investment_portfolio" in tellerOperations
		assert "modify_investment_portfolio" not in tellerOperations
		assert "view_financial_adivisor_contact" not in tellerOperations
		assert "view_financial_planner_contact" not in tellerOperations
		assert "view_money_market_instruments" not in tellerOperations
		assert "view_private_consumer_instruments" not in tellerOperations
	except AssertionError:
		print("Teller RBAC tests failed.")
		tests_failed += 1
		return
	print("Teller RBAC tests passed.")
	tests_passed += 1

if __name__ == "__main__":
	print("\n------------- RBAC Tests -------------")
	test_rbac_client()
	test_rbac_premium_client()
	test_rbac_financial_advisor()
	test_rbac_financial_planner()
	test_rbac_teller()
	print(f"\nRBAC Tests Passed: {tests_passed}")
	print(f"RBAC Tests Failed: {tests_failed}\n")
    
    

	