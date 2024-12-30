# cdk

> AWS 云开发工具包 (CDK) 的命令行工具。
> 更多信息：<https://docs.aws.amazon.com/cdk/latest/guide/cli.html>。

- 列出应用中的堆栈：

`cdk ls`

- 合成并打印指定堆栈的 CloudFormation 模板：

`cdk synth {{stack_name}}`

- 部署一个或多个堆栈：

`cdk deploy {{stack_name1 stack_name2 ...}}`

- 销毁一个或多个堆栈：

`cdk destroy {{stack_name1 stack_name2 ...}}`

- 将指定堆栈与已部署的堆栈或本地 CloudFormation 模板进行比较：

`cdk diff {{stack_name}}`

- 在当前目录为指定的 [l]anguage 创建一个新的 CDK 项目：

`cdk init -l {{language}}`

- 在浏览器中打开 CDK API 参考：

`cdk docs`