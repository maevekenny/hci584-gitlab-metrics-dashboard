from flask_login import UserMixin
from sqlalchemy import Binary, Column, Integer, String
from app import db, login_manager
from app.base.util import hash_pass


class User(db.Model, UserMixin):
    """ 
    This is a class for the user of the system.

    Attributes: 
        model (DefaultMetadata): The database model.
        mixin (UserMixin): The flask_login class expects users to login
    """
    __tablename__ = 'User'

    id = Column(Integer, primary_key=True)
    username = Column(String, unique=True)
    email = Column(String, unique=True)
    password = Column(Binary)
    gitlab_username = Column(String)
    token = Column(String)

    def __init__(self, **kwargs):
        """
        The constructor for User class.

        Parameters:
           self (User): The User object to manipulate.
           kwargs (dict): The dictionary of arguments.
        """
        for property, value in kwargs.items():
            # depending on whether value is an iterable or not, we must
            # unpack it's value (when **kwargs is request.form, some values
            # will be a 1-element list)
            if hasattr(value, '__iter__') and not isinstance(value, str):
                # the ,= unpack of a singleton fails PEP8 (travis flake8 test)
                value = value[0]

            if property == 'password':
                # Encrypt the password so it's not in plain text
                value = hash_pass(value)

            setattr(self, property, value)

    def __repr__(self):
        """
        The function to get the username.

        Parameters:
           self (User): The User object to manipulate.
        """
        return str(self.username)


@login_manager.user_loader
def user_loader(id):
    """
    The function to return the user matching the id.

    Parameters:
        id (string): The id of the user.
    """
    return User.query.filter_by(id=id).first()


@login_manager.request_loader
def request_loader(request):
    """
    The function to retrieve the user based on the request form.

    Parameters:
        request (object): The request form.
    """
    username = request.form.get('username')
    user = User.query.filter_by(username=username).first()
    return user if user else None
