import checker

def main():
    password = input("Enter your password: ")

    errors = checker.check_password(password)

    if not errors :
        print("Password aaapproved!")
    else:
        print("Password does not meet requirements")
        for error in errors:
            print("-", error)

if __name__ == "__main__":
    main()