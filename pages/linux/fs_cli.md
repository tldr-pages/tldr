# fs_cli

> Connect to and control a running FreeSWITCH server using the FreeSWITCH Command Line Interface (ESL client).
> More information: <https://developer.signalwire.com/freeswitch/FreeSWITCH-Explained/Client-and-Developer-Interfaces/1048948/>.

- Connect to the local FreeSWITCH instance:

`fs_cli`

- Connect to a remote FreeSWITCH server:

`fs_cli {{[-H|--host]}} {{host}} {{[-P|--port]}} {{port}} {{[-p|--password]}} {{password}}`

- Execute a single FreeSWITCH command and exit:

`fs_cli {{[-x|--execute]}} "{{command}}"`

- Show FreeSWITCH system status:

`fs_cli {{[-x|--execute]}} "status"`

- Reload FreeSWITCH XML configuration:

`fs_cli {{[-x|--execute]}} "reloadxml"`

- Check if a module is loaded:

`fs_cli {{[-x|--execute]}} "module_exists {{module_name}}"`

- Show active calls:

`fs_cli {{[-x|--execute]}} "show calls"`

- Retry connection on failure:

`fs_cli {{[-r|--retry]}}`
