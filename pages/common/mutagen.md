# mutagen

> Real-time file synchronization and network forwarding tool.
> More information: <https://mutagen.io>.

- Start a synchronization session between a local directory and a remote host:

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} {{user}}@{{host}}:{{/path/to/remote/directory/}}`

- Start a synchronization session between a local directory and a Docker container:

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} docker://{{user}}@{{container_name}}{{/path/to/remote/directory/}}`

- Stop a running session:

`mutagen sync terminate {{session_name}}`

- Start a project:

`mutagen project start`

- Stop a project:

`mutagen project terminate`

- List running sessions for the current project:

`mutagen project list`
