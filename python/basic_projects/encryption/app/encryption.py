from components import cred_loader


# Program Start
def start() -> None:
    credentials: tuple = cred_loader.credentials()
    print(credentials)

start()