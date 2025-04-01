# cdk

> 用于 AWS Cloud Development Kit (CDK) 的命令行界面。
> 更多信息：<https://docs.aws.amazon.com/cdk/latest/guide/cli.html>.

- 列出应用程序中的堆栈：

`cdk ls`

- 为指定的堆栈合成并打印 CloudFormation 模板：

`cdk synth {{stack_name}}`

- 部署一个或多个堆栈：

`cdk deploy {{stack_name1 stack_name2 ...}}`

- 删除一个或多个堆栈：

`cdk destroy {{stack_name1 stack_name2 ...}}`

- 比较指定的堆栈与已部署的堆栈或本地 CloudFormation 模板：

`cdk diff {{stack_name}}`

- 在当前目录中为指定语言创建一个新的 CDK 项目：

`cdk init {{[-l|--language]}} {{language}}`

- 在浏览器中打开 CDK API 参考：

`cdk docs`
