import dns.resolver
from validate_email_address import validate_email

def email_slicer(email):
    try:
        is_valid = validate_email(email, verify=False)

        if is_valid:

            username, domain = email.split('@')

            mx_records = dns.resolver.resolve(domain, 'MX')

            print(f"Username: {username}\nDomain: {domain}")
            print(f"MX Records: {[str(record.exchange) for record in mx_records]}")
        else:
            choice = input("Invalid Email Address\nDo you want to continue (y for yes and n for no)? ").lower()
            if choice == "y":
                user_email = input("Enter a valid email address: ")
                email_slicer(user_email)
            else:
                print("Thank you for using Email Slicer")
                quit()
    except ValueError:
        print("Invalid email address")
    except dns.resolver.NXDOMAIN:
        print(f"The domain does not exist")

user_email = input("Enter your email address: ")

# Call the email_slicer function with the provided email
email_slicer(user_email)
