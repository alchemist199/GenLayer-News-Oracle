# genlayer_oracle.py
from genlayer import *

@gl.contract
class NewsVerifier:
    def __init__(self):
        self.verified_news = gl.Array(gl.String)

    @gl.public
    def fetch_and_verify_news(self, url: gl.String):
        # Menggunakan gl.nondet.web.get sesuai instruksi reviewer
        # Dan dibungkus dengan gl.eq_principle.strict_eq
        with gl.eq_principle.strict_eq:
            response = gl.nondet.web.get(url)
            content = response.text
        
        # Logika verifikasi sederhana
        if "GenLayer" in content:
            self.verified_news.append(url)
            return "News verified and stored on-chain."
        
        return "News not relevant."

    @gl.public
    @gl.view
    def get_latest_news(self) -> gl.Array(gl.String):
        return self.verified_news