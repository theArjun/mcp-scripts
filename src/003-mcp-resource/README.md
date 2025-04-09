# MCP Resource in FastMCP

In the **Model Context Protocol (MCP)**, **resources** are a core component for exposing data to Large Language Models (LLMs) in a secure, standardized way. They function similarly to GET endpoints in a REST API, providing information (e.g., file contents, database schemas, API responses) without performing significant computation or side effects. FastMCP, a Pythonic framework for building MCP servers, simplifies the creation of these resources.

#### How Resources Work in FastMCP:
- **Purpose**: Resources allow LLMs to access data hosted on an MCP server, such as static content or dynamic, parameterized information.
- **Implementation**: Defined using the `@mcp.resource()` decorator, resources can be static or dynamic with templated URIs.
- **Examples**:
  - **Static Resource**:
    ```python
    @mcp.resource("config://app")
    def get_config() -> str:
        """Static configuration data"""
        return "App configuration here"
    ```
  - **Dynamic Resource**:
    ```python
    @mcp.resource("users://{user_id}/profile")
    def get_user_profile(user_id: str) -> str:
        """Dynamic user data"""
        return f"Profile data for user {user_id}"
    ```
- **Automatic Handling**: FastMCP manages MCP protocol details, converting dynamic parameters into MCP templates seamlessly.

#### Key Characteristics:
- **Data-Oriented**: Designed to load information into an LLM’s context, not to execute actions (that’s handled by tools).
- **Flexibility**: Supports various data types, including text and images (via the `Image` class).
- **Integration**: Resources can be accessed within other tools or resources using the `Context` object (e.g., `ctx.read_resource()`).

#### Usage:
Resources are defined in a FastMCP server and made available when the server is run (e.g., via `fastmcp install <file.py>` for Claude Desktop or `fastmcp dev <file.py>` for testing with the MCP Inspector).

#### Why It’s Useful:
MCP resources provide a standardized way to feed LLMs contextual data, and FastMCP makes this process intuitive and efficient for Python developers by minimizing setup complexity.

### Resource in Cursor

https://docs.cursor.com/context/model-context-protocol#mcp-resources

MCP servers offer two main capabilities: tools and resources. Tools are availabe in Cursor today, and allow Cursor to execute the tools offered by an MCP server, and use the output in it’s further steps. However, resources are not yet supported in Cursor. We are hoping to add resource support in future releases.