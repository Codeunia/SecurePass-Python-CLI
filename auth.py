import getpass

MASTER_PASSWORD = "passw@123"

def verify_master_password():
    password = getpass.getpass("Enter master password: ")
    if password == MASTER_PASSWORD:
        print("✅ Access granted!")
        return True
    else:
        print("❌ Access denied! Wrong password.")
        return False