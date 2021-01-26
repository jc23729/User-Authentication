#Password Hashing
# pip install flask-bcrypt(on command line)

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

hashed_password = bcrypt.generate_password_hash(pasword)



