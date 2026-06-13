# ffsend

> Easily and securely share files.
> More information: <https://gitlab.com/timvisee/ffsend>.

- Upload a file:

`ffsend upload {{path/to/file}}`

- Download a file:

`ffsend download {{url}}`

- Upload a file with password:

`ffsend upload {{path/to/file}} {{[-p|--password]}} {{password}}`

- Download a file protected by password:

`ffsend download {{url}} {{[-p|--password]}} {{password}}`

- Upload a file and allow 4 downloads:

`ffsend upload {{path/to/file}} {{[-d|--downloads]}} {{4}}`
