# dotnet

> Cross-platform .NET tools for .NET Core.
> Some subcommands such as `build` and `run` have their own usage documentation.
> More information: <https://learn.microsoft.com/dotnet/core/tools>.

- Initialize a new .NET project:

`dotnet new {{template_short_name}}`

- Add a NuGet package to the project:

`dotnet add package {{package_name}}`

- Restore NuGet packages:

`dotnet restore`

- Build the project and its dependencies:

`dotnet build`

- Build and execute the .NET project:

`dotnet run`

- Execute unit tests in the current directory:

`dotnet test`

- Publish the .NET application for deployment:

`dotnet publish`

- Run a packaged .NET application:

`dotnet {{path/to/application.dll}}`
