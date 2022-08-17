import pytest

from django.urls import reverse

from .models import *
from .serializers import *


@pytest.mark.django_db
def test_list_stores(client):
    url = reverse('stores')
    response = client.get(url)
    stores = Store.objects.all()
    expected_data = StoreSerializer(stores, many=True).data
    assert response.status_code == 200
    assert response.data == expected_data