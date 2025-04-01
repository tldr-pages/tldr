# dotnet test

> 执行 .NET 应用程序的测试。
> 注意：查看 <https://learn.microsoft.com/en-us/dotnet/core/testing/selective-unit-tests> 了解支持的过滤表达式。
> 更多信息：<https://learn.microsoft.com/dotnet/core/tools/dotnet-test>。

- 执行当前目录中的 .NET 项目/解决方案的测试：

`dotnet test`

- 执行特定位置的 .NET 项目/解决方案的测试：

`dotnet test {{path/to/project_or_solution}}`

- 执行与给定过滤表达式匹配的测试：

`dotnet test --filter {{Name~TestMethod1}}`