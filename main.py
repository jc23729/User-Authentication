#Password Hashing
# pip install flask-bcrypt(on command line)

from flask_bcrypt import Bcrypt

bcrypt = Bcrypt()

password = 'supersecretpassword'

bcrypt.generate_password_hash(pasword)



