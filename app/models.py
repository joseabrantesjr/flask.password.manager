from app import db

# The Password class represents a database table with columns for id, name, username, and
# encrypted_password.
class Password(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    username = db.Column(db.String(255), nullable=False)
    encrypted_password = db.Column(db.String(255), nullable=False)

    def __init__(self, name, username, encrypted_password):
        """
        The function is a constructor that initializes the attributes of an object with the given name,
        username, and encrypted password.
        
        :param name: The name parameter is a string that represents the name of the user
        :param username: The username parameter is a string that represents the username of the user
        :param encrypted_password: The encrypted_password parameter is a string that represents the password
        of the user. It is encrypted to ensure security and protect the user's sensitive information
        """
        # The code `self.name = name`, `self.username = username`, and `self.encrypted_password =
        # encrypted_password` are initializing the instance variables of the `Password` class.
        self.name = name
        self.username = username
        self.encrypted_password = encrypted_password
