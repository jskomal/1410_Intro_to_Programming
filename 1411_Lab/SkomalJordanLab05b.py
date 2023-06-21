# Jordan Skomal | 06/20/23
# generates a username and email from user input


def generate_user_email():
    first_name = input("Please enter your first name: ").lower()
    last_name = input("Please enter your last name: ").lower()

    username = f"{last_name}{first_name[0]}"
    email = f"{first_name}.{last_name}@ucdenver.edu"

    print(f"Your username is: {username}")
    print(f"Your email is: {email}")


generate_user_email()
