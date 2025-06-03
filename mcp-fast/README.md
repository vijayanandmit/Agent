#Adding MCP to your python project
If you haven't created a uv-managed project yet, create one:
```bash
uv init mcp-server-demo
cd mcp-server-demo
```

To run server,
```bash
mcp dev server.py
```

Then add MCP to your project dependencies:

```bash
uv add "mcp[cli]"
```
A
lternatively, for projects using pip for dependencies:

```bash
pip install "mcp[cli]"
```

#Running the standalone MCP development tools
To run the mcp command with uv:

```bash
uv run mcp
```


