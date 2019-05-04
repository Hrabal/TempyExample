from app import app, db
from models import Person
from templates.pages import HomePage, PersonPage


@app.route('/')
def index():
    five_people = db.session.query(Person).order_by(Person.second_name, Person.name).limit(5).all()
    return HomePage(data={'people': five_people}).render()


@app.route('/person/<person_id>')
def person(person_id):
    person = db.session.query(Person).filter_by(person_id=person_id).first()
    return PersonPage(data={'person': person}).render()
