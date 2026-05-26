import peewee
from werkzeug.security import generate_password_hash, check_password_hash

from ..db import User


def signup(
        username: str, password: str,
        security_question: str | None = None, security_answer: str | None = None
) -> User | None:
    try:

        if User.query.filter_by(username=username).first():
            return None

        user = User(
            username=username, password=generate_password_hash(password),
        )
        if security_question:
            user.security_question = security_question
            if security_answer:
                user.security_answer = security_answer

        user.save()
        return user

    except peewee.IntegrityError:
        return None
    except peewee.OperationalError:
        return None

    except Exception:
        return None


def authenticate(username: str, password: str) -> User | None:
    try:
        user = User.query.filter_by(username=username).first()
        if user:
            if check_password_hash(user.password, password):
                return user

        return None
    except peewee.IntegrityError:
        return None
    except peewee.OperationalError:
        return None
    except Exception:
        return None


def get_security_question(username: str) -> str | None:
    user = User.query.filter_by(username=username).first()
    if user:
        return user.security_question
    return None


def reset_password(
        username: str, password: str,
        security_answer: str
) -> User | None:
    user = User.query.filter_by(username=username).first()
    if user:
        if user.security_answer and user.security_answer == security_answer:
            user.security_answer = security_answer
            return user
        return None

    return None


def set_security_question(
        user: User, security_question: str,
        security_answer: str
) -> User | None:
    try:
        user.security_question = security_question
        user.security_answer = security_answer
        user.save()
        return user
    except peewee.IntegrityError:
        return None
    except peewee.OperationalError:
        return None
    except Exception:
        return None


def get_user(username: str, password=str) -> User | None:
    return User.get_or_none(username=username, password=password)
