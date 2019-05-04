from tempy.tags import Div

from .base import BasePage


class HomePage(BasePage):
    def init(self):
        self.head(
        )
        self.body.main.container(
            Div(klass="album py-5 bg-light")(
                Div(klass="container")
            )
        )


class PersonPage(BasePage):
        def init(self):
            self.body.main.container.attr(klass="container")
            self.body.main.container(
                Div(klass='row')(
                    Div(klass='col')(
                        self._data['person']
                    )
                ),
                Div(klass='row')(
                    Div(klass='col')(
                        Table(klass='table')(
                            Tr()(c) for c in self._data['person'].contacts
                        )
                    )
                )
            )
