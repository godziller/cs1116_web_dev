from werkzeug.security import generate_password_hash, check_password_hash

"""
Simple generator to get the hash for the 1 Admin User"""

password = 'Admin'

generated = generate_password_hash(password)

print(generated)

password = 'derek'

generated = generate_password_hash(password)

print(generated)