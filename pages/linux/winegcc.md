# winegcc

> GCC wrapper that builds MinGW-compatible Windows binaries under Linux using Winelib.
> More information: <https://manned.org/winegcc>.

- Compile a source file (all standard `gcc` options are passed through):

`winegcc {{[-o]}} {{path/to/output_file}} {{path/to/source.c}}`

- Build a graphical application (links `gdi32`, `comdlg32` and `shell32` by default):

`winegcc {{[-mwindows]}} {{[-o]}} {{path/to/output_file}} {{path/to/source.c}}`

- Build a console application:

`winegcc {{[-mconsole]}} {{[-o]}} {{path/to/output_file}} {{path/to/source.c}}`

- Cross-compile for a specific target architecture:

`winegcc {{[-b|--target]}} {{i386-w64-mingw32}} {{[-o]}} {{path/to/output_file}} {{path/to/source.c}}`

- Use Wine's implementation of MSVCRT instead of the host system libc:

`winegcc {{[-mno-cygwin]}} {{[-o]}} {{path/to/output_file}} {{path/to/source.c}}`
