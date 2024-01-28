# ccache

> C/C++ compiler cache.
> More information: <https://ccache.dev/manual/4.9.html#_command_line_options>.

- Show current cache [s]tatistics:

`ccache -s`

- Clear all [C]ache:

`ccache -C`

- Reset ([z]ero) statistics (but not cache itself):

`ccache -z`

- Compile a file and cache compiled output:

`ccache gcc main.c`

- Create a symlink to ccache to automatically act as the given compiler (note: some symlinked files may already exist in `/usr/lib/ccache/bin/`):

`ln -s /usr/bin/ccache gcc && ./gcc main.c`
