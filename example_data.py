from app import db
from models import Person, Contact
from datetime import date

# Make some instances of Person and Contact
bohumil = Person(name='Bohumil', second_name='Hrabal', birth_date=date(1914, 3, 28))
franz = Person(name='Franz', second_name='Kafka', birth_date=date(1883, 7, 3))
pavel = Person(name='Pavel', second_name='Řezníček', birth_date=date(1942, 1, 30))
egon = Person(name='Egon', second_name='Bondi', birth_date=date(1930, 1, 20))
bohu_mail = Contact(person=bohumil, contact_type='email', value='bohumil@hrabal.com')
franz_mail = Contact(person=franz, contact_type='email', value='frankie@czeckpeople.cz')
franz_phone = Contact(person=franz, contact_type='phone', value='0048 0021 99 777')
franz_mobile = Contact(person=franz, contact_type='mobile', value='320 12 13 144')
bohu_phone = Contact(person=bohumil, contact_type='phone', value='0048 0022 98 788')
pavel_mobile = Contact(person=pavel, contact_type='mobile', value='0048 347 66 666')
egon_facebook = Contact(person=egon, contact_type='facebook', value='https://www.facebook.comprofile.php?id=111222333')

# Save the new entries to the databse
db.session.add(bohumil)
db.session.add(franz)
db.session.add(egon)
db.session.add(pavel)
db.session.add(bohu_mail)
db.session.add(franz_mail)
db.session.add(bohu_mail)
db.session.add(franz_phone)
db.session.add(franz_mobile)
db.session.add(bohu_phone)
db.session.add(pavel_mobile)
db.session.add(egon_facebook)
db.session.commit()
