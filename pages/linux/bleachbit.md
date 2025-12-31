# bleachbit

> Clean junk files on the filesystem.
> More information: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start the graphical user interface (GUI) version of Bleachbit:

`bleachbit --gui`

- Shred a file:

`bleachbit {{[-s|--shred]}} {{path/to/file}}`

- List available cleaner options:

`bleachbit {{[-l|--list-cleaners]}}`

- Preview the files that will be deleted and other changes that will be made before actually performing the clean-up operation:

`bleachbit {{[-p|--preview]}} --preset {{cleaner1.option1 cleaner2.option2 ...}}`

- Perform the clean-up operation and delete files:

`bleachbit {{[-c|--clean]}} --preset {{cleaner1.option1 cleaner2.option2 ...}}`
