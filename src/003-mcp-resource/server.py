from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Resource Demonstration")


@mcp.resource("config://application")
def get_config() -> dict:
    """
    Get the application config.
    """
    return {
        "name": "Resource Demonstration",
        "version": "1.0.0",
        "description": "A demonstration of MCP resources.",
        "author": "Arjun Adhikari",
    }


if __name__ == "__main__":
    mcp.run(transport="stdio")
