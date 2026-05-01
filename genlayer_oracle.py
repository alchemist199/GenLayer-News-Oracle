# genlayer_oracle.py
from genlayer import Contract, Web

class NewsVerifier(Contract):
    def __init__(self):
        self.verified_news = []

    def fetch_and_verify_news(self, url: str):
        # Fitur Intelligent Smart Contract GenLayer untuk membaca web
        web_data = Web.get(url)
        
        # Logika verifikasi sederhana
        if "GenLayer" in web_data.text:
            news_entry = {
                "url": url,
                "status": "Verified",
                "timestamp": "2026-05-01"
            }
            self.verified_news.append(news_entry)
            return "News verified and stored on-chain."
        
        return "News not relevant."

    def get_latest_news(self):
        return self.verified_news