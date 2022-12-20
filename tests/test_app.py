import pytest

from app.setup import App

class TestControllers:

    def test_App(self):
        app = App()
        new_no = app.add_one(1)

        assert (2 == new_no)