# retry

> Repeat command until it succeeds or a criterion is met.
> More information: <https://manned.org/retry>.

- Retry a command until it succeeds:

`retry {{command}}`

- Retry a command every n seconds until it succeeds:

`retry {{[-d|--delay]}} {{n}} {{command}}`

- Give up after n attempts:

`retry {{[-t|--times]}} {{n}} {{command}}`
