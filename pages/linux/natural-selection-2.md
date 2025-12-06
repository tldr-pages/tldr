# Natural Selection 2

> Create and start a headless Natural Selection 2 server.
> More information: <https://naturalselection.fandom.com/wiki/Dedicated_Server.

- Start a server with the default settings:

`{{path/to/server_linux}}`

- Give a server a custom name and connection port:

`{{path/to/server_linux}} -name '{{server_name}}' -port {{27015}}`

- Specify maximum player count:

`{{path/to/server_linux}} -limit {{2..24}}`

- Start a server with webui interface:

`{{path/to/server_linux}} -webadmin -webport {{8080}}`
