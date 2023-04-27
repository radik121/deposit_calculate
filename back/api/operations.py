from dateutil.relativedelta import relativedelta

async def get_calculate_deposit(data):
    result = {}

    start_date = data.date
    amount = data.amount
    rate_month = 1 + data.rate / 12 / 100

    for month in range(data.periods):
        date = start_date + relativedelta(months=+month)
        date_str = date.strftime("%d.%m.%Y")
        amount_month = round(amount * rate_month, 2)
        result[date_str] = amount_month
        amount = amount_month

    return result