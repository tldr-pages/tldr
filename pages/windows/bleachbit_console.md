# bleachbit_console

> Clean junk files on the filesystem.
> More information: <https://docs.bleachbit.org/doc/command-line-interface.html>.

- Start the graphical user interface (GUI) version of Bleachbit:

`bleachbit_console.exe --gui`

- Shred a file:

`bleachbit_console.exe --shred {{path/to/file}}`

- List available cleaner options:

`bleachbit_console.exe --list-cleaners`

- Preview the files that will be deleted and other changes that will be made before actually performing the clean-up operation:

`bleachbit_console.exe --preview {{--preset|cleaner1.option1 cleaner2.* ...}}`

- Perform the clean-up operation and delete files:

`bleachbit_console.exe --clean {{--preset|cleaner1.option1 cleaner2.* ...}}`
