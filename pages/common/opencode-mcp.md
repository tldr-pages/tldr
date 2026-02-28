# opencode mcp

> Manage MCP (Model Context Protocol) servers.
> More information: <https://opencode.ai/docs/cli#mcp>.

- List MCP servers and their status:

`opencode mcp list`

- Add an MCP server interactively:

`opencode mcp add`

- Authenticate with an OAuth-enabled MCP server:

`opencode mcp auth {{server_name}}`

- Remove OAuth credentials for an MCP server:

`opencode mcp logout {{server_name}}`

- Debug OAuth connection for an MCP server:

`opencode mcp debug {{server_name}}`

- Display help:

`opencode mcp {{[-h|--help]}}`
