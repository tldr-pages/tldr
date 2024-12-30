# pulumi 销毁

> 销毁堆栈中的所有现有资源。
> 更多信息：<https://www.pulumi.com/docs/cli/commands/pulumi_destroy/>。

- 销毁当前堆栈中的所有资源：

`pulumi destroy`

- 销毁特定堆栈中的所有资源：

`pulumi destroy --stack {{stack}}`

- 在预览后自动批准并销毁资源：

`pulumi destroy --yes`

- 排除受保护资源不被销毁：

`pulumi destroy --exclude-protected`

- 在堆栈中的所有资源被删除后，移除堆栈及其配置文件：

`pulumi destroy --remove`

- 在遇到错误时继续销毁资源：

`pulumi destroy --continue-on-error`