from flatland import Dict, Form, List, Boolean, String
from flatland.validation import LengthBetween, Present, ValuesEqual

class RegistrationForm(Form):
    username = String.using(
        label='Username',
        validators=[Present(), LengthBetween(4,25)]
    )
    email = String.using(
        label='Email Address',
        optional=True,
        validators=[LengthBetween(6, 35)]
    )
    password = String.using(
        label='New Password',
        validators=[Present()]
    )
    confirm = String.using(
        label='Repeat Password',
        validators=[Present(),
                    ValuesEqual('../confirm', '../password')]
    )
    accept_tos = Boolean.using(
        label='I accept the TOS',
        validators=[Present()]
    )


class PasswordCompareForm(Form):
    password = String.using(
        label='New Password',
        validators=[Present(), LengthBetween(5,25)]
    )
    confirm = String.using(
        label='Repeat Password',
        validators=[Present()]
    )
    validators = [
        ValuesEqual('password', 'confirm')
    ]


class PasswordCompareElement(Form):
    password = String.using(
        label='New Password',
        validators=[Present(), LengthBetween(5, 25)]
    )
    confirm = String.using(
        label='Repeat Password',
        validators=[Present(),
                    ValuesEqual('../confirm', '../password')]
    )


class ContactForm(Form):
    name = String.validated_by(Present())
    addresses = List.of(
        Dict.of(
            String.named('street'),
            String.named('city'),
            String.named('country'),
            List.named('phone_numbers').of(
                Dict.of(
                    String.named('label'),
                    String.named('number')
                )
            ).using(default=1)
        )
    ).using(default=1)


class PhoneNumber(Form):
    label = String
    number = String


class Address(Form):
    street = String
    city = String
    country = String
    phone_numbers = List.of(PhoneNumber).using(default=1)


class ContactForm(Form):
    name = String.validated_by(Present())
    addresses = List.of(Address.using(default=1))

