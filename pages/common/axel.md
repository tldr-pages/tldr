# axel

> Download accelerator.
> Supports HTTP, HTTPS, and FTP.
> More information: <https://github.com/axel-download-accelerator/axel>.

- Download a URL to a file:

`axel {{url}}`

- Download and specify an [o]utput file:

`axel {{url}} -o {{path/to/file}}`

- Download with a specific [n]umber connections:

`axel -n {{connections_num}} {{url}}`

- [S]earch for mirrors:

`axel -S {{mirrors_num}} {{url}}`

- Limit download [s]peed (bytes per second):

`axel -s {{speed}} {{url}}`
