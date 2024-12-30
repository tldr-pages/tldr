# terraform fmt

> 根据 Terraform 语言样式约定格式化配置。
> 更多信息：<https://developer.hashicorp.com/terraform/cli/commands/fmt>。

- 格式化当前目录中的配置：

`terraform fmt`

- 格式化当前目录及子目录中的配置：

`terraform fmt -recursive`

- 显示格式化更改的差异：

`terraform fmt -diff`

- 不将格式化的文件列出到 `stdout`：

`terraform fmt -list=false`