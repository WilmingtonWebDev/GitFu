import re

hogwarts_email_pattern = re.compile('[A-Za-z]{5}@hogwarts.com')

def main(email):
	if hogwarts_email_pattern.match(email):
		return 'Yes'
	return 'No'
