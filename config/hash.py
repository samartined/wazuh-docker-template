import bcrypt

# Your plain text password
password = "your_password_here".encode()

# Generating the salt
salt = bcrypt.gensalt()

# Generating the hash
hashed_password = bcrypt.hashpw(password, salt)

print("Salt:", salt)
print("Hashed Password:", hashed_password)