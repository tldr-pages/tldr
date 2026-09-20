# arthas

> Java diagnostic tool.
> See also: `arthas-watch`, `arthas-trace`.
> More information: <https://arthas.aliyun.com/en/>.

- Start Arthas:

`java -jar {{path/to/arthas-boot.jar}}`

- Reconnect Arthas (default port used by Arthas is 3658):

`telnet localhost {{port_number}}`

- Exit the current Arthas client without affecting other clients, equivalent to `exit`, `logout`, or `q`:

`{{exit|quit|logout|q}}`

- Terminate the Arthas server, disconnecting all the Arthas clients connecting to this server:

`stop`
