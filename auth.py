import os
import hashlib
import getpass

MASTER_PASSWORD_FILE = "master.key"

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def set_master_password():
    password = getpass.getpass("Set your master password: ")
    hashed = hash_password(password)
    with open(MASTER_PASSWORD_FILE, "w") as file:
        file.write(hashed)
    print("✅ Master password set successfully!")

def verify_master_password():
    if not os.path.exists(MASTER_PASSWORD_FILE):
        set_master_password()

    password = getpass.getpass("Enter master password: ")
    hashed = hash_password(password)

    with open(MASTER_PASSWORD_FILE, "r") as file:
        stored_hash = file.read()

    if hashed == stored_hash:
        print("✅ Access granted!")
        return True
    else:
        print("❌ Access denied! Wrong password.")
        return False