# tokei

> A program that prints out statistics about your code.

- Get a report on the code in a folder and all subfolders:

`tokei {{path/to/folder}}`

- Get a report for a folder but ignoring `.min.js` files:

`tokei {{path/to/folder}} -e {{*.min.js}}`

- Print out statistics for individual files in a folder:

`tokei {{path/to/folder}} --files`

- Get a report for all Rust and Markdown files:

`tokei {{path/to/folder}} -t={{Rust}},{{Markdown}}`
