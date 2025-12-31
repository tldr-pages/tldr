# axel

> Download accelerator.
> Supports HTTP, HTTPS, FTP, and FTPs.
> See also: `aria2c`.
> More information: <https://manned.org/axel>.

- Download a URL to a file:

`axel {{url}}`

- Download and specify an output file:

`axel {{url}} {{[-o|--output]}} {{path/to/file}}`

- Download with a specific number connections:

`axel {{[-n|--num-connections]}} {{number}} {{url}}`

- Use a specific number of mirrors for searching and downloading:

`axel {{[-S|--search=]}}{{number}} {{url}}`

- Limit download speed (bytes per second):

`axel {{[-s|--max-speed]}} {{speed}} {{url}}`

- Use the IPv4 protocol only when connecting to the host:

`axel {{[-4|--ipv4]}} {{url}}`

- Limit output to stdout use a custom user-agent when downloading:

`axel {{[-q|--quiet]}} {{[-U|--user-agent]}} {{"Mozilla/5.0"}} {{url}}`
