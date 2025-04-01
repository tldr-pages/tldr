# sc_tracediff

> 显示在路径发生变化时的 traceroute 路径。
> 更多信息：<https://www.caida.org/catalog/software/scamper/>.

- 显示两个 `warts` 文件中 traceroute 的差异：

`sc_tracediff {{path/to/file1.warts}} {{path/to/file2.warts}}`

- 显示两个 `warts` 文件中 traceroute 的差异，包括没有变化的路径：

`sc_tracediff -a {{path/to/file1.warts}} {{path/to/file2.warts}}`

- 显示两个 `warts` 文件中 traceroute 的差异，并尽量显示 DNS 名称而不是 IP 地址：

`sc_tracediff -n {{path/to/file1.warts}} {{path/to/file2.warts}}`
