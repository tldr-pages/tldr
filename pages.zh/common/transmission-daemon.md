# transmission-daemon

> 由 `transmission-remote` 或其 web 界面控制的守护进程。
> 另见： `transmission`。
> 更多信息： <https://manned.org/transmission-daemon>。

- 启动无头的 `transmission` 会话：

`transmission-daemon`

- 启动并监视特定目录中的新种子：

`transmission-daemon --watch-dir {{path/to/directory}}`

- 以 JSON 格式转储守护进程设置：

`transmission-daemon --dump-settings > {{path/to/file.json}}`

- 使用特定设置启动 web 界面：

`transmission-daemon --auth --username {{username}} --password {{password}} --port {{9091}} --allowed {{127.0.0.1}}`