# transmission-daemon

> 由 `transmission-remote` 或其 Web 界面控制的守护进程。
> 参见：`transmission`。
> 更多信息：<https://manned.org/transmission-daemon>。

- 启动一个无头的 `transmission` 会话：

`transmission-daemon`

- 启动并监视特定目录以查找新的种子文件：

`transmission-daemon --watch-dir {{path/to/directory}}`

- 以 JSON 格式导出守护进程设置：

`transmission-daemon --dump-settings > {{path/to/file.json}}`

- 以特定设置启动 Web 界面：

`transmission-daemon --auth --username {{username}} --password {{password}} --port {{9091}} --allowed {{127.0.0.1}}`
