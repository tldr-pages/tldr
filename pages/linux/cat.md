# cat

> Print and concatenate files.
> More information: <https://www.gnu.org/software/coreutils/manual/html_node/cat-invocation.html>.

- Print the contents of a file to `stdout`:

`cat {{path/to/file}}`

- Concatenate several files into an output file:

`cat {{path/to/file1 path/to/file2 ...}} > {{path/to/output_file}}`

- Append several files to an output file:

`cat {{path/to/file1 path/to/file2 ...}} >> {{path/to/output_file}}`

- Write to a file interactively:

`cat > {{path/to/file}}`

- Number all output lines:

`cat {{[-n|--number]}} {{path/to/file}}`

- Display all characters, including tabs, line endings, and non-printing characters:

`cat {{[-A|--show-all]}} {{path/to/file}}`
