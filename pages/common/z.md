# z

> Tracks the most used (by frequency) directories and enables quickly navigating to them using string patterns or `regex`.
> More information: <https://github.com/rupa/z>.

- Go to a directory that contains `string` in the name:

`z string`

- Go to a directory that contains `string1` and then `string2`:

`z string1 string2`

- Go to the highest-ranked directory matching `string`:

`z -r string`

- Go to the most recently accessed directory matching `string`:

`z -t string`

- List all directories in `z`'s database matching `string`:

`z -l string`

- Remove the current directory from `z`'s database:

`z -x`

- Restrict matches to subdirectories of the current directory:

`z -c {{string}}`
