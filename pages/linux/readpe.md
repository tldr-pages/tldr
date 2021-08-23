# readpe

> Displays information about PE files.
> More information: <https://manned.org/readpe>.

- Display all information about the PE file:

`readpe {{path/to/executable}}`

- Display all the headers present in the PE file:

`readpe --all-headers {{path/to/executable}}`

- Display all the sections present in the PE file:

`readpe --all-sections {{path/to/executable}}`

- Display a specific header from the PE file:

`readpe --header {{dos|coff|optional}} {{path/to/executable}}`

- Display imported functions:

`readpe --imports {{path/to/executable}}`

- Display exported functions:

`readpe --exports {{path/to/executable}}`
