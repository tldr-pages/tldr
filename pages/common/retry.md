# retry

> Repeat command until a criteria is met, usually success.
> More information: <https://github.com/minfrin/retry>.

- Retry a command until it succeeds:

`retry {{command}}`

- Retry a command every n seconds until it succeeds:

`retry --delay={{n}} {{command}}`

- Give up after n attempts:

`retry --times={{n}} {{command}}`
