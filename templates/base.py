from app import app
from flask import url_for
from tempy.widgets import TempyPage
from tempy.tags import Link, Script, Meta, Main, Section, Div, H1, P

CONTACTS_ICONS = {
    'email': 'fas fa-envelope',
    'phone': 'fas fa-phone',
    'mobile': 'fas fa-mobile',
    'facebook': 'fab fa-facebook-square'
}

with app.test_request_context():
    HEAD_TAGS = [
        Meta(name="viewport", content="width=device-width, initial-scale=1, shrink-to-fit=no"),
        Link(rel="stylesheet",
             href="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/css/bootstrap.min.css",
             integrity="sha384-PsH8R72JQ3SOdhVi3uxftmaW6Vc51MKb0q5P2rRUpPvrszuE4W1povHYgTpBfshb",
             crossorigin="anonymous"),
        Link(rel="stylesheet", href=url_for('static', filename='style.css'), typ="text/css")
    ]

SCRIPTS = [
    Script(src="https://code.jquery.com/jquery-3.2.1.min.js",
           integrity="sha256-hwg4gsxgFZhOsEEamdOYGBf13FyQuiTwlAQgxVSNgt4=",
           crossorigin="anonymous"),
    Script(src="https://cdnjs.cloudflare.com/ajax/libs/popper.js/1.12.3/umd/popper.min.js",
           integrity="sha384-vFJXuSJphROIrBnz7yo7oB41mKfc8JzQZiCq4NCceLEaO4IHwicKwpJf9c9IpFgh",
           crossorigin="anonymous"),
    Script(src="https://maxcdn.bootstrapcdn.com/bootstrap/4.0.0-beta.2/js/bootstrap.min.js",
           integrity="sha384-alpBpkh1PFOepccYVYDB4do5UnbKysX5WZXm3XxPqe5iKTfUKjNkCk9SaVuEZflJ",
           crossorigin="anonymous"),
    Script(defer=True, src="https://use.fontawesome.com/releases/v5.0.0/js/all.js")
]


class BasePage(TempyPage):
    def init(self):
        self.head(HEAD_TAGS)
        self.body(
            main=Main(role='main')(
                header=Section(klass="jumbotron text-center")(
                    Div(Klass="container")(
                        H1(klass="jumbotron-heading")('TemPy Contact Book'),
                        P(klass="lead text-muted")("A contact book made with TemPy."),
                    )
                ),
                container=Div()
            ),
            scripts=SCRIPTS
        )
