# ccache

> C/C++ compiler cache.
> More information: <https://linux.die.net/man/1/ccache>.

- Show current cache statistics:

`ccache -s`

- Clear all cache:

`ccache -C`

- Reset statistics (but not cache itself):

`ccache -z`

- Compile a file and cache compiled output:

`ccache gcc main.c`

- Create a symlink to ccache to automatically act as the given compiler (note: some symlinked files may already exist in `/usr/lib/ccache/bin/`):

`ln -s /usr/bin/ccache gcc && ./gcc main.c`
