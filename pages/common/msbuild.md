# msbuild

> The Microsoft build tool for Visual Studio project solutions.
> More information: <https://learn.microsoft.com/visualstudio/msbuild>.

- Build the first project file in the current directory:

`msbuild`

- Build a specific project file:

`msbuild {{path/to/project_file}}`

- Specify one or more semicolon-separated targets to build:

`msbuild {{path/to/project_file}} /target:{{targets}}`

- Specify one or more semicolon-separated properties:

`msbuild {{path/to/project_file}} /property:{{name=value}}`

- Specify the build tools version to use:

`msbuild {{path/to/project_file}} /toolsversion:{{version}}`

- Display detailed information at the end of the log about how the project was configured:

`msbuild {{path/to/project_file}} /detailedsummary`

- Display help:

`msbuild /help`
