from auth import verify_master_password
from storage import save_password, get_password, delete_password
import argparse

def main():
    print("🔐 Welcome to SecurePass - Your Local Password Manager")

    if not verify_master_password():
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="add, get, or delete")
    args = parser.parse_args()

    if args.command == "add":
        service = input("Enter the site/service name: ")
        username = input("Enter the username: ")
        password = input("Enter the password: ")
        save_password(service, username, password)
        print("✅ Password saved successfully!")

    elif args.command == "get":
        service = input("Enter the site/service name to retrieve: ")
        entry = get_password(service)
        if entry:
            print(f"Username: {entry['username']}")
            print(f"Password: {entry['password']}")
        else:
            print("❌ No entry found for that service.")

    elif args.command == "delete":  
        service = input("Enter the site/service name to delete: ")
        if delete_password(service):
            print("🗑️ Password deleted successfully.")
        else:
            print("❌ No entry found to delete.")

    else:
        print("❗ Oops! Unknown command. Try: add, get, or delete.")

if __name__ == "__main__":
    main()