import hashlib
import binascii
import os

"""
HCI 584 - Summer 2020
The module that holds utility functions for password encoding.

Reference:  https://www.vitoshacademy.com/hashing-passwords-in-python/

Author: Maeve Kenny
"""


def hash_pass(password):
    """
    The function that hashes a password to be stored.

    Attributes:
        password (string): The password to be encoded

    Returns:
        The encoded password in bytes
    """
    salt = hashlib.sha256(os.urandom(60)).hexdigest().encode('ascii')
    pwdhash = hashlib.pbkdf2_hmac('sha512', password.encode('utf-8'),
                                  salt, 100000)
    pwdhash = binascii.hexlify(pwdhash)
    return (salt + pwdhash)


def verify_pass(provided_password, stored_password):
    """
    The function to verify the password

    Attributes:
        provided_password (string): The password provided to validate
        stored_password (string): The encoded password to validate against

    Returns:
        A boolean of true / false
    """
    stored_password = stored_password.decode('ascii')
    salt = stored_password[:64]
    stored_password = stored_password[64:]
    pwdhash = hashlib.pbkdf2_hmac('sha512',
                                  provided_password.encode('utf-8'),
                                  salt.encode('ascii'),
                                  100000)
    pwdhash = binascii.hexlify(pwdhash).decode('ascii')
    return pwdhash == stored_password
