# dust

> Dust gives an instant overview of which directories are using disk space.
> More information: <https://github.com/bootandy/dust>.

- Display information for the current directory:

`dust`

- Display information for a space-separated list of directories:

`dust {{path/to/directory1}} {{path/to/directory2}}`

- Display 30 directories (defaults to 21):

`dust --number-of-lines {{30}}`

- Show 3 levels of subdirectories:

`dust -d 3`

- Severse order of output, with root at the lowest:

`dust -r`

- Ignore all files and directories with the name 'ignore':

`dust -X ignore`

- Do not display percent bars and percentages:

`dust -b`
