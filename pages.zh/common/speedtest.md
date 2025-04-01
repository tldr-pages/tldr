# speedtest

> 用于通过 <https://speedtest.net> 测试互联网带宽的官方命令行接口。
> 注意：某些平台将 `speedtest` 链接到 `speedtest-cli` 或其他类似工具，如 `librespeed`，在某些 Linux 发行版上也可以安装为 `speedtest`。
> 以下命令示例仅适用于官方客户端。
> 更多信息：<https://www.speedtest.net/apps/cli>.

- 运行速度测试：

`speedtest`

- 运行速度测试并指定输出单位：

`speedtest --unit={{auto-decimal-bits|auto-decimal-bytes|auto-binary-bits|auto-binary-bytes}}`

- 运行速度测试并指定输出格式：

`speedtest --format={{human-readable|csv|tsv|json|jsonl|json-pretty}}`

- 运行速度测试并指定小数点后位数（0 到 8，默认为 2）：

`speedtest --precision={{precision}}`

- 运行速度测试并显示其进度（仅适用于 `human-readable` 和 `json` 输出格式）：

`speedtest --progress={{yes|no}}`

- 列出所有 `speedtest.net` 服务器，并按距离排序：

`speedtest --servers`

- 运行速度测试到特定的 `speedtest.net` 服务器：

`speedtest --server-id={{server_id}}`