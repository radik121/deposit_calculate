import pytest
from httpx import AsyncClient
from app import app

class TestDeposit:
    url = '/api/v1/calculation'

    @pytest.mark.anyio
    async def test_positive_calculat(self, test_client, test_data):

        response = await test_client.post(self.url, json=test_data)
        data = response.json()

        assert response.status_code == 200
        for k, v in data.items():
            assert type(k) == str
            assert type(v) == float
        assert test_data["periods"] == len(data.keys())

    @pytest.mark.anyio
    async def test_negative_calculat(self, test_client, test_bad_data):
        response = await test_client.post(self.url, json=test_bad_data)
        data = response.json()

        assert response.status_code == 400
        assert data['error'] == 'field required'

    @pytest.mark.anyio
    async def test_negative_date(self, test_client, test_bad_date):
        response = await test_client.post(self.url, json=test_bad_date)

        assert response.status_code == 400
        data = response.json()
        assert data['error'] == "time data '31/01/2023' does not match format '%d.%m.%Y'"

    @pytest.mark.anyio
    async def test_negative_periods(self, test_client, test_bad_periods):
        response = await test_client.post(self.url, json=test_bad_periods)

        assert response.status_code == 400
        data = response.json()
        assert data['error'] == "ensure this value is less than or equal to 60"

    @pytest.mark.anyio
    async def test_negative_amount(self, test_client, test_bad_amount):
        response = await test_client.post(self.url, json=test_bad_amount)

        assert response.status_code == 400
        data = response.json()
        assert data['error'] == "ensure this value is greater than or equal to 10000"

    @pytest.mark.anyio
    async def test_negative_rate(self, test_client, test_bad_rate):
        response = await test_client.post(self.url, json=test_bad_rate)

        assert response.status_code == 400
        data = response.json()
        assert data['error'] == "ensure this value is less than or equal to 8"
