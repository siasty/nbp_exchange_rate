from nbp_exchange_rate.nbp_exchange_rate.scheduler.exchange_rates import ExchangeRates
from datetime import datetime


def job():
    currency = ExchangeRates()
    currency.create_currency_exchange(
        date=datetime.today().strftime('%Y-%m-%d'),
        from_currency="EUR",
        to_currency="PLN",
        exchange_rate=currency.get_currancy_rate("EUR")
    )