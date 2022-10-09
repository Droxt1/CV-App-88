from ninja import Schema
from pydantic import EmailStr, Field, UUID4


class CustomerAuthIn(Schema):
    name: str = Field(..., example='John Doe')
    email: EmailStr
    phone: str
    password: str = Field(..., example='password', min_length=8, max_length=32)


class CustomerOut(Schema):
    id: UUID4
    role: str
    name: str
    email: EmailStr
    phone: str

    class Config:
        orm_mode = True


class CompanyAuthIn(Schema):
    name: str
    phone: str
    email: EmailStr
    address: str = Field(..., example='Karada')
    country: str = Field(..., example='Iraq')
    password: str = Field(..., example='password', min_length=8, max_length=32)


class TokenOut(Schema):
    access: str


class CompanyOut(Schema):
    id: UUID4
    role: str
    name: str
    phone: str
    email: EmailStr


class CompanyAuthOut(Schema):
    token: TokenOut
    company: CompanyOut


class CustomerAuthOut(Schema):
    token: TokenOut
    customer: CustomerOut




class Login(Schema):
    email: EmailStr
    password: str = Field(..., example='password', min_length=8, max_length=32)


class LoginOut(Schema):
    token: TokenOut
    role: str
    id: UUID4
    name: str
    email: EmailStr
    phone: str



class LoginWithPhoneOrEmail(Schema):
    email_or_phone: str

    password: str = Field(..., example='password', min_length=8, max_length=32)


class EmailPhoneAuthIn(Schema):
    password: str = Field(..., example='password', min_length=8, max_length=32)
