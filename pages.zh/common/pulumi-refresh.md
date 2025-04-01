# pulumi refresh

> 刷新堆栈中的资源。
> 更多信息：<https://www.pulumi.com/docs/iac/cli/commands/pulumi_refresh/>.

- 比较当前堆栈的状态与云提供商中的状态，并将任何更改合并到当前堆栈中：

`pulumi refresh`

- 刷新当前堆栈中的资源，并以丰富的差异形式显示操作：

`pulumi refresh --diff`

- 刷新当前堆栈中的资源，并在刷新过程中发生任何更改时返回错误：

`pulumi refresh --expect-no-changes`

- 仅预览刷新操作，但不执行刷新：

`pulumi refresh --preview-only`

- 要操作的堆栈名称（默认为当前堆栈）：

`pulumi refresh --stack {{stack_name}}`

- 显示帮助：

`pulumi refresh --help`