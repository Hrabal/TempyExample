from tempy.tags import Div, Table, Tr, A, P, I
from .base import BasePage, CONTACTS_ICONS


class HomePage(BasePage):
    def init(self):
        self.body.main.container.attr(klass="album py-5 bg-light")
        self.body.main.container(
            Div(klass="container")(
                Div(klass='row')(
                    persons=[
                        Div(klass='col-md-4')(
                            Div(klass='card mb-4 shadow-sm')(
                                A(href=f'person/{person.person_id}')(
                                    Div(klass='card-body')(
                                        P(klass='card-text')(
                                            f'{person.name.title()} {person.second_name.title()}'
                                        ),
                                        contacts=[
                                            Div(klass='contactIcon')(
                                                I(klass=CONTACTS_ICONS.get(contact.contact_type, 'noIcon'))
                                            ) for contact in person.contacts
                                        ]
                                    )
                                )
                            )
                        ) for person in self.content_data['people']
                    ]
                )
            )
        )


class PersonPage(BasePage):
        def init(self):
            self.body.main.container.attr(klass="container")
            self.body.main.container(
                Div(klass='row')(
                    Div(klass='col')(
                        self.content_data['person']
                    )
                ),
                Div(klass='row')(
                    Div(klass='col')(
                        Table(klass='table')(
                            Tr()(c) for c in self.content_data['person'].contacts
                        )
                    )
                )
            )
