# terraform plan

> 生成并显示 Terraform 执行计划。
> 更多信息：<https://developer.hashicorp.com/terraform/cli/commands/plan>.

- 生成并显示当前目录中的执行计划：

`terraform plan`

- 显示一个计划，用于销毁当前存在的所有远程对象：

`terraform plan -destroy`

- 显示一个计划，用于更新 Terraform 状态和输出值：

`terraform plan -refresh-only`

- 为输入变量指定值：

`terraform plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- 将 Terraform 的关注点集中在资源的一个子集上：

`terraform plan -target {{resource_type.resource_name[instance_index]}}`

- 以 JSON 格式输出计划：

`terraform plan -json`

- 将计划写入特定文件：

`terraform plan -no-color > {{path/to/file}}`