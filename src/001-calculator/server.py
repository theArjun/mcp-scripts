from fastmcp import FastMCP

mcp = FastMCP("Arjuns Calculator")


@mcp.tool("add", description="Add two numbers")
def add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    return a + b


@mcp.tool("arjun-add", description="Add two numbers with a twist.")
def arjun_add(a: int, b: int) -> int:
    """
    Add two numbers.
    """
    result = a + b
    if result > 10:
        return result % 10
    return result


if __name__ == "__main__":
    mcp.run(transport="stdio")
