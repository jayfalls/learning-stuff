from cryptography.fernet import Fernet
import json
import os
import re


# VARIABLES
## Constants
CRED_ENV: str = "MAILSTOREDLIST"
CRED_PATH: str = ".settings/mailstored"
CRED_KEY_PATH: str = ".settings/multi"


# USER INFO
## Encryption Key
def generate_random_key() -> bytes:
    return Fernet.generate_key()

def store_key(key) -> str:
    with open(CRED_KEY_PATH, 'wb') as file:
        file.write(key)

def create_key() -> None:
    new_key: bytes = generate_random_key()
    store_key(new_key)

def load_key() -> bytes:
    with open(CRED_KEY_PATH, 'rb') as file:
        return file.read()

## Mail Stored
def cred_stored() -> None:
    mail_stored: dict = {CRED_ENV: os.environ.get(CRED_ENV)}
    with open(CRED_PATH, "w") as mail_file:
        json.dump(mail_stored, mail_file)

def cred_unstored() -> None:
    with open(CRED_PATH, "r") as mail_file:
        mail_stored: dict = json.load(mail_file)
    os.environ[CRED_ENV] = mail_stored.get(CRED_ENV, "")

## Credentials
def get_cipher_suite():
    return Fernet(load_key())

def encrypt_credentials(email: str, password: str) -> str:
    cipher_suite = get_cipher_suite()
    credentials: str = f"{email}:{password}"
    encrypted_credentials: bytes = cipher_suite.encrypt(credentials.encode())
    return encrypted_credentials.decode()

def store_credentials(email: str, password: str) -> None:
    encrypted_credentials: str = encrypt_credentials(email, password)
    os.environ[CRED_ENV] = encrypted_credentials
    cred_stored()

def decrypt_credentials(encrypted_credentials: str) -> tuple:
    cipher_suite = get_cipher_suite()
    decrypted_bytes: bytes = cipher_suite.decrypt(encrypted_credentials)
    decrypted_credentials: str = decrypted_bytes.decode()
    return decrypted_credentials.split(':')

def load_credentials() -> tuple:
    retrieved_encrypted_credentials: str = os.environ.get(CRED_ENV)
    credentials: tuple = decrypt_credentials(retrieved_encrypted_credentials)
    return credentials


# INPUT
def get_email():
    while True:
        email = input("Enter your email: ")
        # Basic email format validation using regular expression
        if re.match(r"[^@]+@[^@]+\.[^@]+", email):
            return email
        else:
            print("Invalid email. Please enter a valid email.")

def get_password():
    password = input("Enter your password: ")
    return password

def get_user_credentials() -> None:
    email: str = get_email()
    password: str = get_password()
    create_key()
    store_credentials(email, password)


# INITIALISATION
def init() -> None:
    try:
        with open(CRED_KEY_PATH, 'r') as file:
            cred_unstored()
            print(load_credentials())
            return
    except FileNotFoundError:
        get_user_credentials()
        return
    except PermissionError:
        handlePermissionError()
    except Exception as e:
        print("An error occurred:", str(e)) 