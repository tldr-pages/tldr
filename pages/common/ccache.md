# ccache

> C/C++ compiler cache.
> More information: <https://ccache.dev/manual/latest.html>.

- Show current cache [s]tatistics:

`ccache --show-stats`

- [C]lear all cache:

`ccache --clear`

- Reset ([z]ero) statistics (but not cache itself):

`ccache --zero-stats`

- Compile C code and cache compiled output:

`ccache gcc {{path/to/file.c}}`

- Create a symlink to ccache to automatically act as the given compiler (note: some symlinked files may already exist in `/usr/lib/ccache/bin/`):

`ln -s /usr/bin/ccache gcc && ./gcc main.c`
