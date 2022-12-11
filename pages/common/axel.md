# axel

> Download accelerator.
> Supports HTTP, HTTPS, and FTP.
> More information: <https://github.com/axel-download-accelerator/axel>.

- Download a URL to a file:

`axel {{url}}`

- Download and specify filename:

`axel {{url}} -o {{path/to/file}}`

- Download with multiple connections:

`axel -n {{connections_num}} {{url}}`

- Search for mirrors:

`axel -S {{mirrors_num}} {{url}}`

- Limit download speed (bytes per second):

`axel -s {{speed}} {{url}}`
