# gron

> Transform `JSON` into individual assignments for easier management.
> More information: <https://manned.org/gron>.

- Process `JSON` file into individual assignments:

`gron {{path/to/file|url}}`

- Don't sort output data:

`gron --no-sort {{path/to/file|url}}`

- Disable certificate validation:

`gron {{[-k|--insecure]}} {{url}}`

- Display values of `gron` assignments:

`gron {{[-v|--values]}} {{path/to/file|url}}`

- Turn assignments converted with `gron` back into `JSON`:

`gron {{[-u|--ungron]}} {{path/to/file|url}}`

- Process individual lines of input as separate `JSON` objects:

`gron {{[-s|--stream]}} {{path/to/file|url}}`

- Represent processed data as a `JSON` stream:

`gron {{[-j|--json]}} {{path/to/file|url}}`
