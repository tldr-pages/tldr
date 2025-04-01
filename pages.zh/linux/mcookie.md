# mcookie

> 生成随机的128位十六进制数。
> 更多信息：<https://manned.org/mcookie>.

- 生成一个随机数：

`mcookie`

- 使用文件内容作为随机性种子生成一个随机数：

`mcookie {{[-f|--file]}} {{path/to/file}}`

- 使用文件中的特定字节数作为随机性种子生成一个随机数：

`mcookie {{[-f|--file]}} {{path/to/file}} {{[-m|--max-size]}} {{number_of_bytes}}`

- 打印所使用的随机性详细信息，如每个来源的起源和种子：

`mcookie {{[-v|--verbose]}}`