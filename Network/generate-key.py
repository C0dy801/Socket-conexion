from cryptography.fernet import Fernet

key = Fernet.generate_key()
F = Fernet(key)

print(key)