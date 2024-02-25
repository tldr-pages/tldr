# tokei

> Display statistics about code.
> More information: <https://github.com/XAMPPRocky/tokei>.

- Display a report for the code in a directory and all subdirectories:

`tokei {{path/to/directory}}`

- Display a report for a directory excluding `.min.js` files:

`tokei {{path/to/directory}} -e {{*.min.js}}`

- Display statistics for individual files in a directory:

`tokei {{path/to/directory}} --files`

- Display a report for all files of type Rust and Markdown:

`tokei {{path/to/directory}} -t={{Rust}},{{Markdown}}`
