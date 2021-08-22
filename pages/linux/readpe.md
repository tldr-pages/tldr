# readpe

> Displays information about PE files.
> More information: <https://manpages.debian.org/testing/pev/readpe.1.en.html>.

- Display all information about the PE file:

`readpe {{path/to/binary.exe}}`

- Display all the headers present in the PE file:

`readpe --all-headers {{path/to/binary.exe}}`

- Display all the sections present in the PE file:

`readpe --all-sections {{path/to/binary.exe}}`

- Display a specific header from the PE file:

`readpe --header {{dos|coff|optional}} {{path/to/binary.exe}}`

- Display imported functions:

`readpe --imports {{path/to/binary.exe}}`

- Display exported functions:

`readpe --exports {{path/to/binary.exe}}`
