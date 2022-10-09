from abc import ABC
from typing import Optional, Any
from django.http import HttpRequest
from jose import jwt, JWTError
from ninja.security import HttpBearer
from core import settings
from cv.models import Company, Customer, User


class CompanyAuth(HttpBearer, ABC):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            email = payload.get('email')
            if email:
                return Company.objects.get(email=email)
        except JWTError:
            return {'error': 'unauthorized'}


class CustomerAuth(HttpBearer, ABC):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            email = payload.get('email')
            if email:
                return Customer.objects.get(email=email)
        except JWTError:
            return {'error': 'unauthorized'}


class AuthSuperUser(HttpBearer, ABC):
    def authenticate(self, request: HttpRequest, token: str) -> Optional[Any]:
        try:
            payload = jwt.decode(
                token, settings.SECRET_KEY, algorithms=['HS256'])
            email = payload.get('email')
            if email:
                return User.objects.get(email=email)
        except JWTError:
            return {'error': 'unauthorized'}


def create_superuser_token(User):
    token = jwt.encode({'email': str(User.email)},
                       key=settings.SECRET_KEY, algorithm='HS256')
    return {
        'access': str(token),
    }


def create_company_token(Company):
    token = jwt.encode({'email': str(Company.email), 'phone': str(Company.phone), 'name': str(Company.name)},
                       key=settings.SECRET_KEY, algorithm='HS256')
    return {
        'access': str(token),
    }


def create_customer_token(Customer):
    # token = jwt.encode({'email': str(Customer.email)}, key=settings.SECRET_KEY, algorithm='HS256')
    # return {
    #    'access': str(token),
    # }
    # token contains email and name and phone
    token = jwt.encode({'email': str(Customer.email), 'name': str(Customer.name), 'phone': str(Customer.phone)},
                       key=settings.SECRET_KEY, algorithm='HS256')
    return {
        'access': str(token),
    }


def check_password(password, hashed_password):
    return password == hashed_password
