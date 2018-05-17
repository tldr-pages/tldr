# msbuild

> The Microsoft build tool for .NET projects.

- Build a specific project file:

`msbuild {{path/to/project_file}}`

- Set one or more semicolon-separated targets to build:

`msbuild {{path/to/project_file}} /target:{{targets}}`

- Set one or more semicolon-separated properties:

`msbuild {{path/to/project_file}} /property:{{name=value}}`

- Set the build tools version to use:

`msbuild {{path/to/project_file}} /toolsversion:{{version}}`

- Display detailed information at the end of the log about how the project was configured:

`msbuild {{path/to/project_file}} /detailedsummary`

- Display detailed help information:

`msbuild /help`
