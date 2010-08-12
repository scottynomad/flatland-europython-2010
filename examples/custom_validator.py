from forms import PhoneNumberForm

ff = PhoneNumberForm()
ff.set(dict(country='CA', telephone='+41 22 774 0306'))
ff.validate()
ff.errors
ff['country'] = 'CH'
ff.validate()
