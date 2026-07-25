# fd --format

> Format search results.
> More information: <https://manned.org/fd>.

- Print only the filename:

`fd --format "{/}"`

- Print the parent directory:

`fd --format "{//}"`

- Print the file path without file extension:

`fd --format "{.}"`

- Print only the filename without extension:

`fd --format "{/.}"`

- Prepend a `{` and append a `}` to the results:

`fd --format "\{\{{}\}\}"`

- Prepend text to the results:

`fd --format "{{text}}{}"`
