# TV Trivia Class
import concurrent.futures
from concurrent.futures import ThreadPoolExecutor
import requests


def get_requests() -> list[dict[str]]:
    future_quotes = {}
    quotes = []
    with ThreadPoolExecutor(3) as executor:
        for key_name in ["the_office", "the_simpsons", "breaking_bad"]:
            match key_name:
                case "the_office":
                    future_quotes[key_name] = executor.submit(requests.get, "https://officeapi.dev/api/quotes/random")
                case "the_simpsons":
                    future_quotes[key_name] = executor.submit(requests.get, "https://thesimpsonsquoteapi.glitch.me/quotes")
                case "breaking_bad":
                    future_quotes[key_name] = executor.submit(requests.get, "https://api.breakingbadquotes.xyz/v1/quotes")
        concurrent.futures.wait((future_quotes.values()))
        for quote_key in future_quotes.keys():
            if quote_key == "the_simpsons":
                quotes.append({quote_key: future_quotes[quote_key].result().json()[0]['quote']})
            elif quote_key == "breaking_bad":
                quotes.append({quote_key: future_quotes[quote_key].result().json()[0]['quote']})
            else:
                quotes.append({quote_key: future_quotes[quote_key].result().json()['data']['content']})
        return quotes
