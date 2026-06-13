# ccache

> C/C++ compiler cache.
> Note: Packages usually provide symlinks for compilers in `/usr/lib/ccache/bin`. Prepend this directory to `$PATH` to automatically use `ccache` for them.
> More information: <https://ccache.dev/manual/latest.html>.

- Show current cache statistics:

`ccache {{[-s|--show-stats]}}`

- Clear all cache:

`ccache {{[-C|--clear]}}`

- Reset statistics (but not cache itself):

`ccache {{[-z|--zero-stats]}}`

- Compile C code and cache compiled output (to use `ccache` on all `gcc` invocations, see the note above):

`ccache gcc {{path/to/file.c}}`
