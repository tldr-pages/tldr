# ng build

> Compile an Angular application or library into an output directory named `dist/`.
> More information: <https://angular.dev/cli/build>.

- Build an Angular application or library:

`ng {{[b|build]}}`

- Specify the output path relative to the workspace root:

`ng {{[b|build]}} --output-path {{path/to/directory}}`

- Enable Ahead-of-Time (AOT) compilation:

`ng {{[b|build]}} --aot`

- Show build progress in the console:

`ng {{[b|build]}} --progress`

- Display additional verbose output during the build:

`ng {{[b|build]}} --verbose`

- Automatically clear the terminal screen during rebuilds:

`ng {{[b|build]}} --clear-screen`

- Rebuild automatically when source files change:

`ng {{[b|build]}} --watch`
