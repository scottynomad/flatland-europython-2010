from flatland import DateYYYYMMDD, Dict, Enum, Form, Integer, JoinedString, List, String
from flatland.validation import Converted, Present, ValueGreaterThan

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

PhoneNumberDict = Dict.of(
    String.named('label'),
    String.named('number')
)

class Address(Form):
    street = String
    city = String
    country = String
    phone_numbers = List.of(PhoneNumber).using(default=1)

AddressDict = Dict.of(
    String.named('street'),
    String.named('city'),
    String.named('country'),
    List.named('phone_numbers').of(PhoneNumber)
)

class ContactForm(Form):
    name = String.validated_by(Present())
    addresses = Address.using(default=1)


GuardianContentSearch = Dict.of(
    String.named('q').using(label='Search'
               ).validated_by(Converted()),
    String.named('tag').using(label='Tag filter', optional=True
               ).validated_by(Converted()),
    String.named('section').using(label='Section filter', optional=True
               ).validated_by(Converted()),
    DateYYYYMMDD.named('from-date').using(label='From Date filter', optional=True
               ).validated_by(Converted()),
    DateYYYYMMDD.named('to-date').using(label='To Date filter', optional=True
               ).validated_by(Converted()),
    Enum.named('order-by').valued(['newest', 'oldest', 'relevance']
               ).using(default='newest', optional=True),
    Integer.named('page').using(label='Page Index', default=1
               ).validated_by(Converted(), ValueGreaterThan(0)),
    Integer.named('page-size').using(label='Page Size', default=10
               ).validated_by(Converted(), ValueGreaterThan(0)),
    Enum.named('format').valued(['json', 'xml']).using(default='json'
               ).validated_by(Converted()),
    JoinedString.named('show-fields').using(label='Show fields', default=['all']
               ).validated_by(Converted()),
    JoinedString.named('show-tags').using(label='Show tabs', default=['all']
               ).validated_by(Converted()),
    JoinedString.named('show-refinements').using(label='Show refinements', default=['all']
               ).validated_by(Converted()),
    Integer.named('refinements-size').using(label='Refinement size', default=10
               ).validated_by(Converted(), ValueGreaterThan(0)),
)


