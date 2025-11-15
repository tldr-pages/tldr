# axel

> Download accelerator.
> Supports HTTP, HTTPS, and FTP.
> More information: <https://manned.org/axel>.

- Download a URL to a file:

`axel {{url}}`

- Download and specify an output file:

`axel {{url}} {{[-o|--output]}} {{path/to/file}}`

- Download with a specific number connections:

`axel {{[-n|--num-connections]}} {{connections_num}} {{url}}`

- Search for mirrors:

`axel {{[-S|--search]}} {{mirrors_num}} {{url}}`

- Limit download speed (bytes per second):

`axel {{[-s|--max-speed]}} {{speed}} {{url}}`
