# tofu fmt

> 按照 OpenTofu 语言风格规范格式化配置。
> 更多信息：<https://opentofu.org/docs/cli/commands/fmt/>。

- 格式化当前目录中的配置：

`tofu fmt`

- 格式化当前目录及其子目录中的配置：

`tofu fmt -recursive`

- 显示格式化更改的差异：

`tofu fmt -diff`

- 不列出格式化到 `stdout` 的文件：

`tofu fmt -list=false`