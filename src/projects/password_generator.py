import string
import secrets


def password_generator():
    alphabet = string.ascii_letters + string.digits + string.punctuation
    password = "".join(secrets.choice(alphabet) for _ in range(12))
    return password


if __name__ == "__main__":
    print(password_generator())
