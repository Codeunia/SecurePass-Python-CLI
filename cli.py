from auth import verify_master_password
from storage import save_password, get_password, delete_password, list_services, clear_all_passwords
import argparse

def main():
    print("🔐 Welcome to SecurePass - Your Local Password Manager")

    if not verify_master_password():
        return

    parser = argparse.ArgumentParser()
    parser.add_argument("command", help="add, get, delete, list, or clear")
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

    elif args.command == "list":
        list_services()

    elif args.command == "clear":
        confirm = input("⚠️ Are you sure you want to delete ALL saved entries? (yes/no): ")
        if confirm.lower() == "yes":
            clear_all_passwords()
        else:
            print("❎ Operation cancelled.")

    else:
        print("❗ Oops! Unknown command. Try: add, get, delete, list, or clear.")

if __name__ == "__main__":
    main()