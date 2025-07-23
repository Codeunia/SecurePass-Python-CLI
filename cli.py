import argparse

def main():
    print("🔐 Welcome to SecurePass - Your Local Password Manager")

    parser = argparse.ArgumentParser()
    parser.add_argument("command")
    args = parser.parse_args()

    if args.command == "add":
        print("🔐 You chose to add a new password.")
    elif args.command == "get":
        print("🔍 You chose to retrieve a password.")
    elif args.command == "delete":
        print("🗑️ You chose to delete a password.")
    else:
        print("❗ Oops! Unknown command. Try: add, get, or delete.")

if __name__ == "__main__":
    main()
