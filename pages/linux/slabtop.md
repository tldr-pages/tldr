# slabtop

> Display kernel slab cache information in real time.
> See also: `top`, `htop`, `atop`.
> More information: <https://manned.org/slabtop>.

- Start `slabtop`:

`sudo slabtop`

- Sort by cache size:

`sudo slabtop {{[-s|--sort]}} c`

- Sort by number of objects:

`sudo slabtop {{[-s|--sort]}} {{number}}`

- Sort by object size:

`sudo slabtop {{[-s|--sort]}} {{object_size}}`

- Display once and then exit:

`sudo slabtop {{[-o|--once]}}`

- Display help:

`slabtop {{[-h|--help]}}`
