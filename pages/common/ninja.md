# ninja

> A Build system designed to be fast.
> More information: <https://ninja-build.org/manual.html>.

- Build in the current directory:

`ninja`

- Build in the current directory, executing 4 [j]obs at a time in parallel:

`ninja -j {{4}}`

- Build a program in a given directory:

`ninja -C {{path/to/directory}}`

- Show [t]argets (e.g. `install` and `uninstall`):

`ninja -t targets`

- Display verbose output:

`ninja {{[-v|--verbose]}}`

- Display help:

`ninja -h`
