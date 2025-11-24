# pygbag

> Package Pygame projects as WebAssembly to run in web browsers.
> More information: <https://github.com/pygame-web/pygbag#pygbag>.

- Package a Pygame project and start a local test server:

`pygbag {{path/to/project_folder}}`

- Package using Python module syntax:

`python -m pygbag {{path/to/project_folder}}`

- Package and build without starting the test server:

`pygbag {{path/to/project_folder}} --build`

- Package with a specific template:

`pygbag {{path/to/project_folder}} --template {{template_name.tmpl}}`

- Package and create a ZIP archive for <https://itch.io>:

`pygbag {{path/to/project_folder}} --archive`

- Package with optimization turned off:

`pygbag {{path/to/project_folder}} --no_opt`

- Specify a custom port for the test server:

`pygbag {{path/to/project_folder}} --port {{8080}}`

- Display help:

`pygbag {{[-h|--help]}}`
