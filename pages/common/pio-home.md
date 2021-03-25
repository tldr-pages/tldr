# pio home

> Launch the PlatformIO Home web server.
> More information: <https://docs.platformio.org/en/latest/core/userguide/cmd_home.html>.

- Open PlatformIO Home in the default web browser:

`pio home`

- Use a specific HTTP port (defaults to 8008):

`pio home --port {{port}}`

- Bind to a specific IP address (defaults to 127.0.0.1):

`pio home --host {{ip_address}}`

- Do not automatically open PlatformIO Home in the default web browser:

`pio home --no-open`

- Automatically shutdown the server on timeout (in seconds) when no clients are connected:

`pio home --shutdown-timeout {{time}}`

- Specify a unique session identifier to keep PlatformIO Home isolated from other instances and protected from 3rd party access:

`pio home --session-id {{id}}`
