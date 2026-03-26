# meson

> SCons-like build system that uses Python as a front-end language and Ninja as a building backend.
> More information: <https://mesonbuild.com/Commands.html>.

- Generate a project with default values:

`meson init`

- Generate a C project with a given name and version:

`meson init {{[-l|--language]}} c {{[-n|--name]}} {{myproject}} --version {{0.1}}`

- Configure a directory named `build` with default values for compilation:

`meson {{[build|setup build]}}`

- Compile the project:

`meson compile -C {{path/to/build_directory}}`

- Run all tests in the project:

`meson test`

- Install the project to `/usr/local`

`meson install -C {{build}}`

- Display help:

`meson {{[-h|--help]}}`

- Display version:

`meson {{[-v|--version]}}`
