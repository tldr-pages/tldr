# ccache

> C/C++ compiler cache.
> Note: packages usually provide symlinks for compilers in `/usr/lib/ccache/bin`. Prepend this directory to `$PATH` to automatically use `ccache` for them.
> More information: <https://ccache.dev/manual/latest.html>.

- Show current cache [s]tatistics:

`ccache --show-stats`

- [C]lear all cache:

`ccache --clear`

- Reset ([z]ero) statistics (but not cache itself):

`ccache --zero-stats`

- Compile C code and cache compiled output (to use `ccache` on all `gcc` invocations, see the note above):

`ccache gcc {{path/to/file.c}}`
