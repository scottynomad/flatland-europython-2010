import xodb
from xodb import Schema, String, Array

class Department(object):

  def __init__(self, name, employees):
      self.name = name
      self.employees = employees



class DepartmentSchema(Schema):
    language = String.using(default="en")
    name = String.using(facet=True)
    employees = Array.of(String.using(facet=True))


db = xodb.temp()
db.map(Department, DepartmentSchema)

housing = Department("housing", ['bob', 'jane'])
monkeys = Department("monkeys", ['bob', 'rick'])

db.add(housing, monkeys)
db.backend.flush()

assert db.query("name:monkeys").next().name == "monkeys"
assert db.query("employees:jane").next().name == "housing"


