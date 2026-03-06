import requests

def conversion():
    url = "https://api.frankfurter.app/latest"
    response = requests.get(url)
    start = str(input("Enter the 3 letter code for original currency: ")).upper()
    end = str(input("Enter the 3 letter code for converted currency: ")).upper()
    amount = float(input("Amount: "))
    if start == "EUR" or end =="EUR":
        eur_converter(start, end, amount, response)
    else:
        current_rate(start, end, amount, response)

def current_rate(start, end, amount, response):
    if response.status_code == 200:
        original = response.json()["rates"][start]
        convert = response.json()["rates"][end]
        value = amount * (convert / original)
        print(round(value, 2), end)
        print("Conversion units against 1 Euro:\n", original, start, convert, end)
    else:
        print(f"Error: {response.status_code}")

def eur_converter(start, end, amount, response):
    value = 0
    if start == "EUR":
        if response.status_code == 200:
            convert = response.json()["rates"][end]
            value = amount  * convert
        else:
            print(f"Error: {response.status_code}")
    elif end == "EUR":
        if response.status_code == 200:
            original = response.json()["rates"][start]
            value = amount / original 
        else:    
            print(f"Error: {response.status_code}")
    print(round(value, 2), end)

def currencies():
    available = ["AUD BGN BRL CAD CHF CNY CZK DKK EUR GBP HKD HUF IDR ILS INR ISK JPY KRW MXN MYR NOK NZD PHP PLN RON SEK SGD THB TRY USD ZAR"]
    print("Following are currencies available for conversion. Base is in Euros:\n", available)
    conversion()

currencies()
