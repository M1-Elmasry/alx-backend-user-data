#!/usr/bin/env python3
"""
    module for authentication operations
"""
from typing import List, TypeVar
from flask import request


class Auth:
    """ Auth class
    """

    def require_auth(self, path: str, excluded_paths: List[str]) -> bool:
        """
        Return: False if @path in @excluded_paths otherwise True

        Note: each path in @exculded_paths should ended with /
        """

        if path is None or excluded_paths is None:
            return True

        if path[-1] != '/':
            path += '/'

        return False if path in excluded_paths else True

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
