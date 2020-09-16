# dotnet publish

> Publish a .NET application and its dependencies to a folder for deployment to a hosting system.
> More information: <https://docs.microsoft.com/dotnet/core/tools/dotnet-publish>.

- Compile a .NET project in release mode:

`dotnet publish --configuration Release {{path/to/project_file}}`

- Publish the .NET Core runtime with your application for the specified runtime:

`dotnet publish --self-contained true --runtime {{runtime_identifier}} {{path/to/project_file}}`

- Package the application into a platform-specific single-file executable:

`dotnet publish --runtime {{runtime_identifier}} -p:PublishSingleFile=true {{path/to/project_file}}`

- Trim unused libraries to reduce the deployment size of an application:

`dotnet publish --self-contained true --runtime {{runtime_identifier}} -p:PublishTrimmed=true {{path/to/project_file}}`

- Compile a .NET project without restoring dependencies:

`dotnet publish --no-restore {{path/to/project_file}}`

- Specify the output directory:

`dotnet publish --output {{path/to/directory}} {{path/to/project_file}}`
