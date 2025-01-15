# arthas

> Java diagnostic tool.
> See also: `arthas-watch`, `arthas-trace`.
> More information: <https://arthas.aliyun.com/en/>.

- Start arthas:

`java -jar arthas-boot.jar`

- Reconnect arthas:

`telnet localhost 3658`

- Exit the current Arthas client without affecting other clients. equals `exit`、`logout`、`q` command:

`exit|quit|logout|q`

- Terminate the Arthas server, all the Arthas clients connecting to this server will be disconnected:

`stop`
