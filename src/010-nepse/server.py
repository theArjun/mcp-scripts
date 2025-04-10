from mcp.server.fastmcp import FastMCP
import httpx

BASE_URL = "https://data.nepse.bot"

mcp = FastMCP(
    "Nepal Stock Exchange (Nepse) API",
    dependencies=[
        "httpx",
    ],
)


@mcp.tool("fetch_nepse_point", description="Fetch the current NEPSE point.")
def fetch_nepse_point():
    """
    Fetch the current NEPSE point.
    """
    url = f"{BASE_URL}/todays-index/NEPSE"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from NEPSE API"}


@mcp.tool(
    "fetch_top_gainers", description="Fetch the top gainers stocks in NEPSE."
)
def fetch_top_gainers():
    """
    Fetch the top gainers in NEPSE.
    """
    url = f"{BASE_URL}/top-gainer"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from NEPSE API"}


@mcp.tool(
    "fetch_top_losers", description="Fetch the top losers stocks in NEPSE."
)
def fetch_top_losers():
    """
    Fetch the top losers in NEPSE.
    """
    url = f"{BASE_URL}/top-loser"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from NEPSE API"}


@mcp.tool(
    "fetch_top_turnover", description="Fetch the top turnover stocks in NEPSE."
)
def fetch_top_turnover():
    """
    Fetch the top turnover in NEPSE.
    """
    url = f"{BASE_URL}/top-turnover"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from NEPSE API"}


@mcp.tool(
    "fetch_top_volume", description="Fetch the top volume stocks in NEPSE."
)
def fetch_top_volume():
    """
    Fetch the top volume in NEPSE.
    """
    url = f"{BASE_URL}/top-volume"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from NEPSE API"}


@mcp.tool(
    "fetch_top_transaction",
    description="Fetch the top transaction stocks in NEPSE.",
)
def fetch_top_transaction():
    """
    Fetch the top transaction in NEPSE.
    """
    url = f"{BASE_URL}/top-transaction"
    response = httpx.get(url)
    if response.status_code == 200:
        data = response.json()
        return data
    else:
        return {"error": "Failed to fetch data from NEPSE API"}
