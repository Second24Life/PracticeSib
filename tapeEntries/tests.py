from django.test import TestCase
from django.url import revesre


class HomeTests(TestCase):
    def tets_home_view_code(self):
        url = revesre('index')
        response = self.client.get(url)
        self.assertEquals(response.status_code, 200)
