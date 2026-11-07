# dotnet add

> Add package or project references to a .NET project.
> Some subcommands such as `package` and `reference` have their own usage documentation.
> More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet>.

- Add a NuGet package to the project in the current directory:

`dotnet add package {{package}}`

- Add a NuGet package to a specific project:

`dotnet add {{path/to/project.csproj}} package {{package}}`

- Add a project reference to the project in the current directory:

`dotnet add reference {{path/to/reference.csproj}}`

- Add a project reference to a specific project:

`dotnet add {{path/to/project.csproj}} reference {{path/to/reference.csproj}}`

- Display help:

`dotnet add --help`
