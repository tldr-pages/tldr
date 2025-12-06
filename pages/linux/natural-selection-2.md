# Natural Selection 2

> Create and start a headless Natural Selection 2 server.
> More information: <https://naturalselection.fandom.com/wiki/Dedicated_Server.

- Start a server with the default settings:

`{{path/to/server_linux}}`

- Give a server a custom name that shows in the server browser:

`{{path/to/server_linux}} -name '{{server_name}}'`

- Specify a connection port for the server:

`{{path/to/server_linux}} -port {{27015}}`

- Specify maximum player count:

`{{path/to/server_linux}} -limit {{2..24}}`

- Specify the initial map the server starts on:

`{{path/to/server_linux}} -map {{ns2_summit}}`

- Limit access to the server with a password:

`{{path/to/server_linux}} -password {{password}}`

- Start a server with webui admin interface:

`{{path/to/server_linux}} -webadmin -webport {{8080}}`
