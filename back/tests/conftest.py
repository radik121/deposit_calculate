import pytest_asyncio
from httpx import AsyncClient
from app import app

@pytest_asyncio.fixture(scope="function")
async def test_client():
    async with AsyncClient(app=app, base_url="http://test") as c:
        yield c

@pytest_asyncio.fixture()
async def test_data():
    data = {
        "date": "31.01.2023",
        "periods": 7,
        "amount": 10000,
        "rate": 6
    }
    return data

@pytest_asyncio.fixture()
async def test_bad_data():
    data = {
        "date": "31.01.2023",
        "periods": 7
    }
    return data

@pytest_asyncio.fixture()
async def test_bad_date():
    data = {
        "date": "31/01/2023",
        "periods": 7,
        "amount": 10000,
        "rate": 6
    }
    return data

@pytest_asyncio.fixture()
async def test_bad_periods():
    data = {
        "date": "31.01.2023",
        "periods": 65,
        "amount": 10000,
        "rate": 6
    }
    return data

@pytest_asyncio.fixture()
async def test_bad_amount():
    data = {
        "date": "31.01.2023",
        "periods": 6,
        "amount": 1000,
        "rate": 6
    }
    return data

@pytest_asyncio.fixture()
async def test_bad_rate():
    data = {
        "date": "31.01.2023",
        "periods": 6,
        "amount": 10000,
        "rate": 9
    }
    return data