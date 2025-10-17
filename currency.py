import requests

def get_all_fiat_rates(base="GBP"):
    url = f"https://open.er-api.com/v6/latest/{base}"
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        data = response.json()

        if "rates" not in data:
            print("⚠️ Unexpected response format:")
            print(data)
            return {}

        print(f"💱 Exchange rates for 1 {base}:")
        for currency, rate in sorted(data["rates"].items()):
            print(f"  {currency}: {rate:.4f}")

        return data["rates"]

    except requests.exceptions.RequestException as e:
        print(f"⚠️ Network error: {e}")
        return {}

# Example usage
get_all_fiat_rates("GBP")