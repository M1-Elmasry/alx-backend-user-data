#!/usr/bin/env python3
"""
    module for authentication operations
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_path: List[str]) -> bool:
        """
        will implement later
        """
        return False

    def authorization_header(self, request=None) -> str:
        """
        will implement later
        """
        return None

    def current_user(self, request=None) -> TypeVar('User'):
        """
        will implement later
        """
        return None
