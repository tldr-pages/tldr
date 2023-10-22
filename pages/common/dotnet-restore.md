# dotnet restore

> Restores the dependencies and tools of a .NET project.
> More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-restore>.

- Restore dependencies for a .NET project or solution in the current directory:

`dotnet restore`

- Restore dependencies for a .NET project or solution in a specific location:

`dotnet restore {{path/to/project_or_solution}}`

- Restore dependencies without caching the HTTP requests:

`dotnet restore --no-cache`

- Force all dependencies to be resolved even if the last restore was successful:

`dotnet restore --force`

- Restore dependencies using package source failures as warnings:

`dotnet restore --ignore-failed-sources`

- Restore dependencies with a specific verbosity level:

`dotnet restore --verbosity {{quiet|minimal|normal|detailed|diagnostic}}`
