from django.test import TestCase
from rest_framework.test import APIClient, APITestCase
from rest_framework import status


class MyTest(APITestCase):
    
    def test_post_data_not_logged_in(self):
        response = self.client.post('/data_store/data/test/test/', {'test_submission': True}, format='json')
        self.assertTrue(status.is_client_error(response.status_code))

