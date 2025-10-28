# dutree

> A tool that uses colorful text-based trees to analyze file system usage.
> More information: <https://github.com/nachoparker/dutree/blob/master/README.md>

- Show a graphical tree of the current directory:

`dutree`

- Show a specific directory:

`dutree {{path/to/dir}}`

- Aggregate items smaller than a number of KB (or M for MB, or G for GB):

`dutree --aggr {{number}}K`

- Show subdirectories up to the specified depth (default is 1):

`dutree --depth {{depth}}`

- Skip directories for a fast local overview:

`dutree --files-only`

- Exclude hidden files:

`dutree --no-hidden`
