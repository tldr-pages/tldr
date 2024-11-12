# dotnet test

> Execute tests for a .NET application.
> Note: View <https://learn.microsoft.com/en-us/dotnet/core/testing/selective-unit-tests> for supported filter expressions.
> More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-test>.

- Execute tests for a .NET project/solution in the current directory:

`dotnet test`

- Execute tests for a .NET project/solution in a specific location:

`dotnet test {{path/to/project_or_solution}}`

- Execute tests matching the given filter expression:

`dotnet test --filter {{Name~TestMethod1}}`
