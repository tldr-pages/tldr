# ctags

> Generates an index (or tag) file of language objects found in source files for many popular programming languages.
> More information: <https://ctags.io/>.

- Generate tags for a single file, and save them in a file named "tags" in the current directory:

`ctags {{path/to/file}}`

- Generate tags for all files in the current directory and save them in a file with a custom filename:

`ctags -f {{filename}} *`

- Generate tags for all files in the current directory and all subdirectories (-R, --recurse):

`ctags -R`
