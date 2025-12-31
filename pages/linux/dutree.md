# dutree

> Analyze file system usage with colorful text-based trees.
> More information: <https://github.com/nachoparker/dutree#usage>.

- Show a graphical tree of the current directory:

`dutree`

- Show a specific directory:

`dutree {{path/to/directory}}`

- Aggregate items smaller than a number of KB (or M for MB, or G for GB):

`dutree --aggr {{number}}K`

- Show subdirectories up to the specified depth (default is 1):

`dutree --depth {{depth}}`

- Skip directories for a fast local overview:

`dutree --files-only`

- Exclude hidden files:

`dutree --no-hidden`
