# terraform 计划

> 生成并显示 Terraform 执行计划。
> 更多信息：<https://developer.hashicorp.com/terraform/cli/commands/plan>。

- 在当前目录中生成并显示执行计划：

`terraform plan`

- 显示销毁当前存在的所有远程对象的计划：

`terraform plan -destroy`

- 显示更新 Terraform 状态和输出值的计划：

`terraform plan -refresh-only`

- 为输入变量指定值：

`terraform plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- 将 Terraform 的注意力集中在仅一部分资源上：

`terraform plan -target {{resource_type.resource_name[instance index]}}`

- 将计划输出为 JSON：

`terraform plan -json`

- 将计划写入特定文件：

`terraform plan -no-color > {{path/to/file}}`