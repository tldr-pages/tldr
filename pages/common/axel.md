# axel

> Download accelerator
> Supports HTTP, HTTPS, and FTP

- Download a URL to a file

`axel {{url}}`

- Download and rename

`axel {{url}} -o {{filename}}`

- Download with multiple connections

`axel -n {{20}} {{url}}`

- Search for mirrors (can specify numbers)

`axel -S {{5}} {{url}}`

- Limit download speed (bytes per second)

`axel -s {{10000}} {{url}}`