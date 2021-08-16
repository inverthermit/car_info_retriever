import datetime
from uuid import UUID
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class CarTests(APITestCase):
    fixtures = ["info_service/fixtures/coreapp_seeds.json"]

    def test_exact_search(self):
        url = reverse("exact_search_car")
        # Test non existing name
        data = {"name": "non-existing name"}
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"result": None})

        # Test existing name
        data = {"name": "vw pickup"}
        expected_result = {
            "result": {
                "acceleration": 24,
                "cylinders": 4,
                "displacement": 97,
                "horsepower": 52,
                "id": UUID("00000000-0000-0000-0000-000000000192"),
                "miles_per_gallon": 44,
                "name": "vw pickup",
                "origin": "Europe",
                "weight_in_lbs": 2130,
                "year": datetime.date(1982, 1, 1),
            }
        }
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

        return

    def test_term_search(self):
        url = reverse("term_search_car")
        # Test non existing term
        data = {"term": "non-existing term"}
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, {"result": []})

        # Test existing term
        data = {"term": "bmw"}
        expected_result = {
            "result": [
                {
                    "id": UUID("00000000-0000-0000-0000-00000000001d"),
                    "name": "bmw 2002",
                    "miles_per_gallon": 26,
                    "cylinders": 4,
                    "displacement": 121,
                    "horsepower": 113,
                    "weight_in_lbs": 2234,
                    "acceleration": 12,
                    "year": datetime.date(1970, 1, 1),
                    "origin": "Europe",
                },
                {
                    "id": UUID("00000000-0000-0000-0000-0000000000f9"),
                    "name": "bmw 320i",
                    "miles_per_gallon": 21,
                    "cylinders": 4,
                    "displacement": 121,
                    "horsepower": 110,
                    "weight_in_lbs": 2600,
                    "acceleration": 12,
                    "year": datetime.date(1977, 1, 1),
                    "origin": "Europe",
                },
            ]
        }
        response = self.client.get(url, data, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, expected_result)

        return
