markup = """
    <form xmlns="http://www.w3.org/1999/xhtml"
          xmlns:py="http://genshi.edgewall.org/"
          xmlns:form="http://ns.discorporate.us/flatland/genshi"
          form:bind="form">
      <form:with auto_domid="on" auto_for="on">
        <label py:with="el=form.password" form:bind="el">
          ${el.label}: <input form:bind="el" />
        </label>

        <label py:with="el=form.confirm" form:bind="el">
          ${el.label}: <input form:bind="el" />
        </label>

        <button value="Submit" />
      </form:with>
    </form>

"""

from genshi.template import MarkupTemplate
from flatland import Form, String
from flatland.validation import Present, LengthBetween, ValuesEqual
from flatland.out.genshi_06 import setup

class PasswordCompareElement(Form):
    password = String.using(
        label='New Password',
        validators=[
            Present(),
            LengthBetween(5, 25)
        ]
    )
    confirm = String.using(
        label='Repeat Password',
        validators=[
            Present(),
            ValuesEqual(
                '../confirm',
                '../password'
            )]
    )



template = MarkupTemplate(markup)
setup(template)

kw = dict(form=PasswordCompareElement())
output = template.generate(**kw).render('xhtml')
print output
