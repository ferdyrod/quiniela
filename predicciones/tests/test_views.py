from django.test import TestCase, Client


class ViewTest(TestCase):
    """Testing of the views for the 'predicciones' app"""
    def setUp(self):
        self.client_stub = Client()

    def test_view_home_route(self):
        response = self.client_stub.get('/')
        self.assertEquals(response.status_code, 200)