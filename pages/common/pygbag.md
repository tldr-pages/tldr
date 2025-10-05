# pygbag

> Package Pygame projects as WebAssembly to run in web browsers.
> More information: <https://pygame-web.github.io>.

- Package a Pygame project and start a local test server:

`pygbag {{path/to/project_folder}}`

- Package using Python module syntax:

`python -m pygbag {{path/to/project_folder}}`

- Package and build without starting the test server:

`pygbag --build {{path/to/project_folder}}`

- Package with a specific template:

`pygbag --template {{template_name.tmpl}} {{path/to/project_folder}}`

- Package and create a ZIP archive for itch.io:

`pygbag --archive {{path/to/project_folder}}`

- Package with optimization turned off:

`pygbag --no_opt {{path/to/project_folder}}`

- Specify a custom port for the test server:

`pygbag --port {{8080}} {{path/to/project_folder}}`

- Display help information:

`pygbag --help`
