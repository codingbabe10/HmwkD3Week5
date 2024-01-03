from marshmallow import Schema, fields, post_load


class Person(object):
    def __init__(self,name,age):
        self.name = name
        self.age = age 

    def __repr__(self):
        return f'{self.name} is {self.age} years old.'

class PersonSchema(Schema) :
    name = fields.String()
    age = fields.Integer()

    @post_load
    def create_person(self, data, **kwargs):
        return Person(**data)


input_data = {}

input_data['name']= input ('what is your name?')
input_data['age']= input ('what is your age?')

schema = PersonSchema()
result = schema.load(input_data)

# person = person(name=input_data['name'], age=input_data['age'])

    
# print(person)

result = schema.dump(person)

print (result)