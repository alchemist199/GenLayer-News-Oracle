from genlayer import *

# Simple global state
verified_news = Array(String)

@gl.public
def verify_news(url: String):
    # Standard function for non-deterministic web fetch
    def fetch_data():
        response = gl.nondet.web.get(url)
        return response.text

    # Canonical consensus pattern
    content = gl.eq_principle.strict_eq(fetch_data)
    
    if "GenLayer" in content:
        verified_news.append(url)
        return "Success: News verified on-chain!"
    
    return "Failed: GenLayer not mentioned."

@gl.public
@gl.view
def get_history() -> Array(String):
    return verified_news