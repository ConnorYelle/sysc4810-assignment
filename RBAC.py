
#Dictionary mapping operations to roles that have access to them
OPERATION_ROLES = {
	"view_account_balance": ["Client", "Premium Client", "Financial Advisor", "Financial Planner", "Teller"],
	"view_investment_portfolio": ["Client", "Premium Client", "Financial Advisor", "Financial Planner", "Teller"],
	"modify_investment_portfolio": ["Premium Client", "Financial Advisor", "Financial Planner"],
	"view_financial_adivisor_contact": ["Client", "Premium Client"],
	"view_financial_planner_contact": ["Premium Client"],
	"view_money_market_instruments": ["Financial Planner"],
	"view_private_consumer_instruments": ["Financial Advisor", "Financial Planner"],
}

#Function to check if a user has access to a specific operation
def check_access(user, operation):
	if operation == "view_account_balance":
		if user.roles in OPERATION_ROLES["view_account_balance"]:
			return True

	elif operation == "view_investment_portfolio":
		if user.roles in OPERATION_ROLES["view_investment_portfolio"]:
			return True

	elif operation == "modify_investment_portfolio":
		if user.roles in OPERATION_ROLES["modify_investment_portfolio"]:
			return True

	elif operation == "view_financial_adivisor_contact":
		if user.roles in OPERATION_ROLES["view_financial_adivisor_contact"]:
			return True

	elif operation == "view_financial_planner_contact":
		if user.roles in OPERATION_ROLES["view_financial_planner_contact"]:
			return True	

	elif operation == "view_money_market_instruments":
		if user.roles in OPERATION_ROLES["view_money_market_instruments"]:
			return True

	elif operation == "view_private_consumer_instruments":
		if user.roles in OPERATION_ROLES["view_private_consumer_instruments"]:
			return True	
	return False

#Function to get all permitted operations for a user
def get_permitted_operations(user):
	permitted_operations = []
	for operation, roles in OPERATION_ROLES.items():
		if user.role in roles:
			permitted_operations.append(operation)
	return permitted_operations


 
 
	