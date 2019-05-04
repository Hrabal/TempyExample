from tempy import TempyREPR
from tempy.tags import Span, B
from app import db


class Person(db.Model):
    person_id = db.Column(db.Integer,
                          primary_key=True,
                          autoincrement=True)
    name = db.Column(db.String(255),
                     index=True,
                     nullable=False)
    second_name = db.Column(db.String(255),
                            index=True)
    birth_date = db.Column(db.Date)

    def __repr__(self):
        return f'<Person: {self.name} {self.second_name}>'

    class PersonREPR(TempyREPR):
        def repr(self):
            self(
                Span(klass='personData')(B()('Name: '), self.name),
                Span(klass='personData')(B()('Second Name: '), self.second_name),
                Span(klass='personData')(B()('Birthday: '), self.birth_date.isoformat())
            )


class Contact(db.Model):
    contact_id = db.Column(db.Integer,
                           primary_key=True,
                           autoincrement=True)
    person_id = db.Column(db.Integer,
                          db.ForeignKey('person.person_id'))
    person = db.relationship('Person',
                             backref='contacts',
                             foreign_keys=[person_id])
    contact_type = db.Column(db.String(10),
                             index=True,
                             nullable=False)
    value = db.Column(db.String(255))

    def __repr__(self):
        return f'<Contact {self.contact_type} of {self.person}: {self.value}>'

    class Tr(TempyREPR):
        def repr(self):
            self(
                Td()(self.contact_type.title()),
                Td()(self.value)
            )
