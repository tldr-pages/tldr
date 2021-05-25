# dust

> Dust gives an instant overview of which directories are using disk space.
> More information: <https://github.com/bootandy/dust>.

- Display information for the current directory:

`dust`

- Display information for a space-separated list of directories:

`dust {{path/to/directory1}} {{path/to/directory2}}`

- Display 30 directories (defaults to 21):

`dust --number-of-lines {{30}}`

- Display information for the current directory, up to 3 levels deep:

`dust --depth {{3}}`

- Display the biggest directories at the top in descending order:

`dust --reverse`

- Ignore all files and directories with a specific name:

`dust --ignore-directory {{file_or_directory_name}}`

- Do not display percent bars and percentages:

`dust --no-percent-bars`
