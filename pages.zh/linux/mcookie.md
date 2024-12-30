# mcookie

> 生成随机的128位十六进制数字。
> 更多信息：<https://manned.org/mcookie>。

- 生成一个随机数：

`mcookie`

- 使用文件的内容作为随机性的种子生成一个随机数：

`mcookie --file {{path/to/file}}`

- 使用文件中的特定字节数作为随机性的种子生成一个随机数：

`mcookie --file {{path/to/file}} --max-size {{number_of_bytes}}`

- 打印所使用随机性的详细信息，如每个来源的来源和种子：

`mcookie --verbose`