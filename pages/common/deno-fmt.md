# deno fmt

> Format source files.
> More information: <https://docs.deno.com/runtime/reference/cli/fmt/>.

- Format all supported files in the current directory recursively:

`deno fmt`

- Format specific files or directories:

`deno fmt {{path/to/file_or_directory1 path/to/file_or_directory2 ...}}`

- Check formatting without modifying files:

`deno fmt --check {{path/to/file_or_directory}}`

- Watch for changes and automatically format files:

`deno fmt --watch {{path/to/file_or_directory}}`

- Format files while ignoring a specific directory:

`deno fmt --ignore={{path/to/ignored_directory}} {{path/to/directory}}`

- Format code from `stdin` and print the result to `stdout`:

`echo "{{markdown_text}}" | deno fmt --ext {{md}} -`
