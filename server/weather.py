from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("weather")


if __name__ == "__main__":
    mcp.run(transport="stdio")
