import os
import smtplib
import sys
from components import cred_loader


# VARIABLES
## Constants
READ_PERMISSION_ERROR_RESPONSE: str = "PermissionError with the file structure. Reinstall the program in a place where it can access its files.\nOr run as sudo (NOT RECOMMENDED)."


# PROGRAM CONTROL
def stop_program() -> None:
    sys.exit()

def handlePermissionError() -> None:
    print(READ_PERMISSION_ERROR_RESPONSE)
    stop_program()


# SMTP
def smtp_start() -> None:
    server = smtplib.SMTP("smtp.gmail.com", 25)

    server.ehlo()

    #server.login("mail@mail.com", "123Password")


# Program Start
def start() -> None:
    cred_loader.init()

start()