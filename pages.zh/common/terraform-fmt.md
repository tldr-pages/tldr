# terraform fmt

> 根据 Terraform 语言的样式规范格式化配置。
> 更多信息：<https://developer.hashicorp.com/terraform/cli/commands/fmt>。

- 格式化当前目录中的配置：

`terraform fmt`

- 格式化当前目录及其子目录中的配置：

`terraform fmt -recursive`

- 显示格式化更改的差异：

`terraform fmt -diff`

- 不将已格式化的文件列表输出到 `stdout`：

`terraform fmt -list=false`
