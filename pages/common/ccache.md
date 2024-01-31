# ccache

> C/C++ compiler cache.
> Note: ccache can also mock a compiler by changing the executable's name. Packages usually provide symlinks for common compilers at `/usr/lib/ccache/bin`. Prepend this directory to `$PATH` to automatically use ccache for these compilers.
> More information: <https://ccache.dev/manual/latest.html>.

- Show current cache [s]tatistics:

`ccache --show-stats`

- [C]lear all cache:

`ccache --clear`

- Reset ([z]ero) statistics (but not cache itself):

`ccache --zero-stats`

- Compile C code and cache compiled output (for better usage, see note above):

`ccache gcc {{path/to/file.c}}`
