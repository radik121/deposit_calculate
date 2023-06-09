# Deposit calculation

В проекте применен следующий стек технологий:
- FastAPI
- Uvicorn
- Pytest
- Docker, docker-compose


## Задание
Необходимо создать REST API для рассчета депозита.
Пример входных данных:
  ```python
  {
    "date": "31.01.2023",
    "periods": 3,
    "amount": 10000,
    "rate": 6
  }
  ```


##### Условия:
- При успешном рассчете HTTP-статус ответа 200.
  Ответ в формате json:
  ```python
  {
    "31.01.2023": 10050,
    "28.02.2023": 10100.25,
    "31.03.2023": 10150.75
  }
  ```
- Если валидация входных данных не пройдена, HTTP-статус ответа 400.
  Ответ в формате json:
  ```python
  {
    "error": "текст ошибки"
  }
  ```

##### Start

1. Склонировать репозиторий

```python
git clone https://github.com/radik121/deposit_calculate.git
```

2. Перейти в деркторию с проектом

```python
cd deposit_calculate
```

3. Запустить web-приложение в контейнере Docker

```python
docker-compose up -d
```

4. Запустить тесты для api-запросов

```python
docker-compose -f docker-compose.test.yml up
```
 #### post запрос отправляется на адрес: http://0.0.0.0:8000/api/v1/calculation
 #### Документация OpenAPI: http://0.0.0.0:8000/api/v1/docs