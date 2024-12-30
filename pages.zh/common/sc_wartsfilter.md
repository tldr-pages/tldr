# sc_wartsfilter

> 从 `warts` 文件中选择特定记录。
> 更多信息：<https://www.caida.org/catalog/software/scamper/>.

- 过滤所有具有特定目的地的数据记录，并将其写入单独的文件：

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{192.0.2.5}} -a {{192.0.2.6}}`

- 过滤所有在某个前缀中具有特定目的地的记录，并将其写入单独的文件：

`sc_wartsfilter -i {{path/to/input.warts}} -o {{path/to/output.warts}} -a {{2001:db8::/32}}`

- 过滤所有使用特定操作的记录，并将其输出为 JSON 格式：

`sc_wartsfilter -i {{path/to/input.warts}} -t {{ping}} | sc_warts2json`