# dotnet tool

> Manage .NET tools and search published tools in NuGet.
> More information: <https://docs.microsoft.com/dotnet/core/tools/global-tools>.

- Install Entity Framework Core as a global tool:

`dotnet tool install --global dotnet-ef`

- Install tools defined in the local tool manifest:

`dotnet tool restore`

- Update a specific global tool:

`dotnet tool update --global {{tool_name}}`

- Uninstall a local tool (use `--global` for global tools):

`dotnet tool uninstall {{tool_name}}`

- List installed local tools (use `--global` for global tools):

`dotnet tool list`

- Search tools in NuGet:

`dotnet tool search {{search_term}}`

- Display help:

`dotnet tool --help`
