from werkzeug.security import check_password_hash

from ..db import User


class UserSession:
    """A Global session manager for the application"""

    def __init__(self, user: User | None = None):
        self._current_user = user

    @property
    def current_user(self) -> User | None:
        """Returns the current user"""
        return self._current_user

    def set_user(self, user: User):
        self._current_user = user

    def verify_user(self, password: str) -> bool:
        return check_password_hash(self._current_user.password, password) if self._current_user else False

    @property
    def xor_key(self) -> int | None:
        return int(self._current_user.password) if self._current_user else None

    @property
    def security_question_exists(self) -> bool:
        return True if self._current_user and self._current_user.security_question  else False
