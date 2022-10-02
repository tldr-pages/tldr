# dotnet tool

> Manage .NET tools and search published tools in NuGet.
> More information: <https://learn.microsoft.com/dotnet/core/tools/global-tools>.

- Install a global tool (don't use `--global` for local tools):

`dotnet tool install --global {{dotnetsay}}`

- Install tools defined in the local tool manifest:

`dotnet tool restore`

- Update a specific global tool (don't use `--global` for local tools):

`dotnet tool update --global {{tool_name}}`

- Uninstall a global tool (don't use `--global` for local tools):

`dotnet tool uninstall --global {{tool_name}}`

- List installed global tools (don't use `--global` for local tools):

`dotnet tool list --global`

- Search tools in NuGet:

`dotnet tool search {{search_term}}`

- Display help:

`dotnet tool --help`
