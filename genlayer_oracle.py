# genlayer_oracle.py
from genlayer import *

@gl.contract
class NewsVerifier:
    def __init__(self):
        self.verified_news = gl.Array(gl.String)

    @gl.public
    def verify_news(self, url: gl.String):
        # Define internal function for non-deterministic data fetching
        def fetch_data():
            response = gl.nondet.web.get(url)
            return response.text

        # Call the function via strict_eq for consensus safety
        content = gl.eq_principle.strict_eq(fetch_data)
        
        # Verification logic
        if "GenLayer" in content:
            self.verified_news.append(url)
            return "Success: News verified on-chain!"
        
        return "Failed: GenLayer not mentioned."

    @gl.public
    @gl.view
    def get_history(self) -> gl.Array(gl.String):
        return self.verified_news