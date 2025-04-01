# hexyl

> 一个简单的终端用十六进制查看器。使用彩色输出区分不同类别的字节。
> 更多信息：<https://github.com/sharkdp/hexyl>.

- 打印文件的十六进制表示：

`hexyl {{path/to/file}}`

- 打印文件前 n 个字节的十六进制表示：

`hexyl -n {{n}} {{path/to/file}}`

- 打印文件中第 512 到 1024 个字节：

`hexyl -r {{512}}:{{1024}} {{path/to/file}}`

- 从第 1024 个字节开始打印 512 个字节：

`hexyl -r {{1024}}:+{{512}} {{path/to/file}}`
