# Prompt user to enter an email address
email = input("Enter email address: ")

# Initialize the validity of the email to False
is_valid = False

# Check if the email contains '@'
if "@" in email:
    # Split the email into name and domain parts
    at_position = email.find("@")
    name = email[:at_position]
    domain = email[at_position + 1:]

    # Check if the domain contains a period
    if "." in domain:
        # Split the domain into main domain and suffix
        dot_position = domain.rfind(".")
        domain_main = domain[:dot_position]
        domain_suffix = domain[dot_position + 1:]

        # Check if the domain suffix has at least two characters
        if len(domain_suffix) >= 2:
            is_valid = True

# Print the result
print(is_valid)
