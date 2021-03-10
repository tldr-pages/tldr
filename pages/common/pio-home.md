# pio home

> Launch PlatformIO Home Web-server.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- Set specific HTTP port for the server (defaults to 8008):

`pio home --port {{port}}`

- Set specific HTTP host for the server (defaults to 127.0.0.1):

`pio home --host {{host}}`

- Do not automatically open PlatformIO Home in a system web browser:

`pio home --no-open`

- Automatically shutdown the server on timeout (in seconds) when no clients are connected:

`pio home --shutdown-timeout {{time}}`

- Specify a unique session identifier to keep PlatformIO Home isolated from other instances and protected from 3rd party access:

`pio home --session-id {{id}}`
