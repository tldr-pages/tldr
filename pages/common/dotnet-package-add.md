# dotnet package add

> Add or update a NuGet package reference in a .NET project.
> Available since .NET 10; for older SDKs, use `dotnet add package`.
> More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-package-add>.

- Add a package to the project in the current directory:

`dotnet package add {{package}}`

- Add a package to a specific project:

`dotnet package add {{package}} --project {{path/to/project.csproj}}`

- Display help:

`dotnet package add --help`
