# Context in FastMCP

## Example:

```python
from mcp.server.fastmcp import FastMCP, Context

mcp = FastMCP("My App")

@mcp.tool()
async def long_task(files: list[str], ctx: Context) -> str:
    """Process multiple files with progress tracking"""
    for i, file in enumerate(files):
        ctx.info(f"Processing {file}")
        await ctx.report_progress(i, len(files))
        data, mime_type = await ctx.read_resource(f"file://{file}")
    return "Processing complete"
```

In your example, Context is passed as an argument (ctx: Context) to an asynchronous tool function (long_task) 
decorated with @mcp.tool(). This suggests it’s a built-in object that provides methods to interact with the MCP 
runtime environment. Think of it as a Swiss Army knife for your tools—offering utilities like logging, progress 
updates, and resource access without you needing to reinvent the wheel.


From this, we see three explicit uses of Context:

1. ctx.info(): Logging or outputting informational messages.
2. await ctx.report_progress(): Reporting task progress asynchronously.
3. await ctx.read_resource(): Accessing file data and metadata (e.g., MIME type).