# dotnet run

> Run a .NET application without explicit compile or launch commands.
> More information: <https://learn.microsoft.com/dotnet/core/tools/dotnet-run>.

- Run the project in the current directory:

`dotnet run`

- Run a specific project:

`dotnet run --project {{path/to/file.csproj}}`

- Run the project with specific arguments:

`dotnet run -- {{arg1=foo arg2=bar ...}}`

- Run the project using a target framework moniker:

`dotnet run --framework {{net7.0}}`

- Specify architecture and OS, available since .NET 6 (Don't use `--runtime` with these options):

`dotnet run --arch {{x86|x64|arm|arm64}} --os {{win|win7|osx|linux|ios|android}}`
