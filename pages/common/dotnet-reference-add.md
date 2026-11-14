# dotnet reference add

> Add project-to-project references to a .NET project.
> Available since .NET 10; for older SDKs, use `dotnet add reference`.
> More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-reference-add>.

- Add a reference to the project in the current directory:

`dotnet reference add {{path/to/reference.csproj}}`

- Add a reference to a specific project:

`dotnet reference add {{path/to/reference.csproj}} --project {{path/to/project.csproj}}`

- Display help:

`dotnet reference add --help`
