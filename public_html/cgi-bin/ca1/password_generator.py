from werkzeug.security import generate_password_hash, check_password_hash
password = 'Admin'

generated = generate_password_hash(password)

print(generated)