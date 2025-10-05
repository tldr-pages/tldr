# pygbag

> Build and serve Python projects for the web (WebAssembly) using Emscripten.
> Used mainly with pygame-based applications.
> More information: <https://pygame-web.github.io/wiki/pygbag/>.

- Build the current Python project into a web bundle:
`pygbag build`

- Serve the web bundle locally on port 8000:
`pygbag serve --port {{8000}}`

- Specify a different directory to serve:
`pygbag serve {{path/to/build_directory}}`

- Clean previously generated build artifacts:
`pygbag clean`

- Enable debug mode while serving:
`pygbag serve --debug`

- Export a project to a distributable zip file:
`pygbag export`

- Show available templates for web packaging:
`pygbag --template`

- Display help for all commands:
`pygbag --help`
