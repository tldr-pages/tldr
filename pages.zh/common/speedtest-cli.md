# speedtest-cli

> 使用 <https://speedtest.net> 测试互联网带宽。
> 另见：`speedtest` 官方 CLI。
> 更多信息：<https://github.com/sivel/speedtest-cli>。

- 运行速度测试：

`speedtest-cli`

- 运行速度测试并以字节为单位显示值，而不是位：

`speedtest-cli --bytes`

- 运行速度测试并使用 `HTTPS`，而不是 `HTTP`：

`speedtest-cli --secure`

- 运行速度测试，但不执行下载测试：

`speedtest-cli --no-download`

- 运行速度测试并生成结果的图像：

`speedtest-cli --share`

- 列出所有 `speedtest.net` 服务器，按距离排序：

`speedtest-cli --list`

- 运行速度测试，指定 `speedtest.net` 服务器：

`speedtest-cli --server {{server_id}}`

- 运行速度测试并以 JSON 格式显示结果（不显示进度信息）：

`speedtest-cli --json`