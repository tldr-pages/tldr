# mutagen

> Real-time file synchronization and network forwarding tool.
> More information: <https://mutagen.io/documentation/introduction/>.

- Start a synchronization session between a local directory and a remote host:

`mutagen sync create --name={{session_name}} /{{path/to/local_directory}}/ {{user}}@{{host}}:/{{path/to/remote_directory}}/`

- Start a synchronization session between a local directory and a Docker container:

`mutagen sync create --name={{session_name}} /{{path/to/local_directory}}/ docker://{{user}}@{{container_name}}/{{path/to/remote_directory}}/`

- Stop a running session:

`mutagen sync terminate {{session_name}}`

- Start a project:

`mutagen project start`

- Stop a project:

`mutagen project terminate`

- List running sessions for the current project:

`mutagen project list`
