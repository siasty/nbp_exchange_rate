import requests
import frappe

class ExchangeRates:
    def get_currancy_rate(self,currency:str):
        url = f"https://api.nbp.pl/api/exchangerates/rates/a/{currency.lower()}/?format=json"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            return data['rates'][0]['mid']
        else:
            return 0
        
    def create_currency_exchange(self,date, from_currency, to_currency, exchange_rate):
        try:
            # Create a new Currency Exchange document
            currency_exchange = frappe.get_doc({
                "doctype": "Currency Exchange",
                "date": date,
                "from_currency": from_currency,
                "to_currency": to_currency,
                "exchange_rate": exchange_rate,
                "for_buying":True,
                "for_selling":True
            })
        
            currency_exchange.insert()
        
            frappe.db.commit() 
            return currency_exchange

        except Exception as e:
            frappe.throw(f"Error creating Currency Exchange: {str(e)}")    