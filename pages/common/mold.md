# mold

> A modern linker, and a faster drop-in replacement for GNU `ld`.
> See also: `ld`.
> More information: <https://github.com/rui314/mold/blob/main/docs/mold.md>.

- Run a build command such as `make`, `ninja`, or `cargo`, with `mold` used in place of `ld`:

`mold --run {{command}} {{arguments}}`

- Link object files into an executable:

`mold {{path/to/file1.o path/to/file2.o ...}} {{[-o|--output]}} {{path/to/output_executable}}`

- Link object files into a shared library:

`mold --shared {{path/to/file1.o path/to/file2.o ...}} {{[-o|--output]}} {{path/to/library.so}}`

- Link an object file with a library located in a specific directory:

`mold {{path/to/file.o}} {{[-L|--library-path]}} {{path/to/library_directory}} -l{{library_name}}`

- Print which input files depend on which others for each symbol:

`mold --print-dependencies {{path/to/file1.o path/to/file2.o ...}} {{[-o|--output]}} {{path/to/output_executable}}`
