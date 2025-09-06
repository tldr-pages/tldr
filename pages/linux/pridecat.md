# pridecat

> Like cat but more colorful.
> More information: <https://github.com/lunasorcery/pridecat>.

- Print the contents of a file in pride colors to `stdout`:

`pridecat {{path/to/file}}`

- Print contents of a file in trans colors:

`pridecat {{path/to/file}} {{[--trans|--transgender]}}`

- Alternate between lesbian and bisexual pride flags:

`pridecat {{path/to/file}} --lesbian {{[--bi|--bisexual]}}`

- Print contents of a file with the background colors changed:

`pridecat {{path/to/file}} {{[-b|--background]}}`

- List directory contents in pride flag colors:

`ls | pridecat --{{flag}}`
