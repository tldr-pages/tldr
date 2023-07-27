# ninja

> A Build system designed to be fast.
> More information: <https://ninja-build.org/manual.html>.

- Build in the current directory:

`ninja`

- Build in the current directory, executing 4 jobs at a time in parallel:

`ninja -j {{4}}`

- Build a program in a given directory:

`ninja -C {{path/to/directory}}`

- Show targets (e.g. `install` and `uninstall`):

`ninja -t targets`

- Show help:

`ninja -h`
