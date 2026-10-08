import re

EMAIL_PATTERN = r'[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9.-]+'


def find_emails(text):
    return re.findall(EMAIL_PATTERN, text)


def is_valid_email(email):
    return re.fullmatch(EMAIL_PATTERN, email) is not None


# Find emails in text
text = """
Contact us at support@example.com
or sales.team@company.co.in
You can also email rahul_23@gmail.com
"""

emails = find_emails(text)

print("Emails found:")
for email in emails:
    print(email)

# Validate an email
email = input("\nEnter an email to validate: ")

if is_valid_email(email):
    print("Valid Email")
else:
    print("Invalid Email")