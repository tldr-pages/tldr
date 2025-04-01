# tofu plan

> 生成并显示 OpenTofu 执行计划。
> 更多信息：<https://opentofu.org/docs/cli/commands/plan/>.

- 在当前目录生成并显示执行计划：

`tofu plan`

- 显示一个摧毁所有现有远程对象的计划：

`tofu plan -destroy`

- 显示一个更新 Tofu 状态和输出值的计划：

`tofu plan -refresh-only`

- 指定输入变量的值：

`tofu plan -var '{{name1}}={{value1}}' -var '{{name2}}={{value2}}'`

- 将 Tofu 的注意力集中于资源的一个子集：

`tofu plan -target {{resource_type.resource_name[instance index]}}`

- 以 JSON 格式输出计划：

`tofu plan -json`

- 将计划写入特定文件：

`tofu plan -no-color > {{path/to/file}}`