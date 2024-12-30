# 速度测试

> 官方命令行界面，用于测试互联网带宽，网址为 <https://speedtest.net>。
> 注意：某些平台将 `speedtest` 链接到 `speedtest-cli` 或其他工具，如 `librespeed`，这些工具也可以在某些 Linux 发行版上安装为 `speedtest`。
> 这些命令示例仅适用于官方客户端。
> 更多信息请访问：<https://www.speedtest.net/apps/cli>。

- 运行速度测试：

`speedtest`

- 运行速度测试并指定输出单位：

`speedtest --unit={{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- 运行速度测试并指定输出格式：

`speedtest --format={{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- 运行速度测试并指定使用的小数点位数（0到8，默认值为2）：

`speedtest --precision={{precision}}`

- 运行速度测试并打印其进度（仅适用于输出格式 `human-readable` 和 `json`）：

`speedtest --progress={{yes|no}}`

- 列出所有 `speedtest.net` 服务器，按距离排序：

`speedtest --servers`

- 对特定的 `speedtest.net` 服务器进行速度测试：

`speedtest --server-id={{server_id}}`