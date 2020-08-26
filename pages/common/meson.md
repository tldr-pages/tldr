# meson

> SCons-like build system that uses python as a front-end language and Ninja as a building backend.
> More information: <https://mesonbuild.com/>.

- Generate a c project with name myproject and version 0.1:

`meson init --language={{c}} --name={{myproject}} --version={{0.1}}`

- Configure builddir with default values:

`meson setup {{builddir}}`

- Build the project:

`meson compile -C {{builddir}}`

- Show help message:

`meson --help`

- Show version info:

`meson --version`
