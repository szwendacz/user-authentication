import hashlib
import pyotp


def hash_user_password(password):
    return hashlib.sha256(password.encode('utf-8')).hexdigest()


def check_auth(code):
    totp = pyotp.TOTP("TGHAXM2M3WVUL224")
    auth = totp.now()
    return auth == code



