from django.test import TestCase
from rest_framework import status
from rest_framework.test import APIClient, APITestCase
from django.contrib.auth.models import User
from .models import Record
from rest_framework_simplejwt.tokens import RefreshToken

from django.urls import reverse

# Create your tests here.

class RecordTests(APITestCase):

    # Arrange, act, assert

    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.other_user = User.objects.create_user(username='otheruser', password='otherpassword')

        self.client = APIClient()
        
        self.refresh = RefreshToken.for_user(self.user)
        self.client.credentials(HTTP_AUTHORIZATION='Bearer ' + str(RefreshToken.for_user(self.user).access_token))

        self.record = Record.objects.create(user=self.user, data='test data') 
    
    def test_list_records(self):
        url = reverse('record-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data['results']), 1)

    def test_create_record(self):
        url = reverse('record-list')
        data = {'data': 'test data'}
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Record.objects.count(), 2)
        self.assertEqual(Record.objects.get(id=2).data, 'test data')

    def test_get_record(self):
        url = reverse('record-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['results'][0]['data'], 'test data')

    def test_update_record(self):
        #Partial update
        url = reverse('record-detail', args=[self.record.id])
        data = {'data': 'updated data'}
        response = self.client.patch(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.record.refresh_from_db()
        self.assertEqual(self.record.data, 'updated data')

    def test_delete_record(self):
        url = reverse('record-detail', args=[self.record.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Record.objects.count(), 0)
