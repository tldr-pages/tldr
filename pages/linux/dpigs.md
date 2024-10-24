# dpigs

> Show which installed packages occupy the most space on `apt` based systems.
> Sort the installed packages by size and output the largest ones.
> More information: <https://manned.org/man/dpigs>.

- Display the N largest packages on the system:

`dpigs --lines={{N}}`

- Use the specified file instead of the default dpkg [s]tatus file:

`dpigs --status={{path/to/file}}`

- Display the largest [S]ource packages of binary packages installed on the system:

`dpigs --source`

- Display package sizes in [H]uman-readable format:

`dpigs --human-readable`

- Display help:

`dpigs --help`


