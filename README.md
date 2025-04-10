# MCP Scripts

## Path for Claude Config:


`$HOME/Library/Application Support/Claude/claude_desktop_config.json`


## Path for Cursor Config:
`{$PROJECT_DIR}/.cursor/mcp.json`


## Path for vscode insiders
`$HOME/Library/Application Support/Code - Insiders/User/settings.json`

or project specific (explore on your own.)

## Available transport modes:

1. stdio
2. sse

## Adding dependencies:

```python
mcp = FastMCP(
    "MCP App Name",
    dependencies=[
        "httpx",
        "python-dotenv",
    ],
)
```

## Add mcp settings in cursor


Configuring MCP Servers
The MCP configuration file uses a JSON format with the following structure:

```json
{
  "mcpServers": {
    "server-name": {
      "command": "python",
      "args": ["mcp-server.py"],
      "env": {
        "API_KEY": "value"
      }
    }
  }
}
```
The env field allows you to specify environment variables that will be available to your MCP server process. This is particularly useful for managing API keys and other sensitive configuration.