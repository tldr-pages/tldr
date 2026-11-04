# jj unsign

> Drop cryptographic signatures from revisions.
> See also: `jj sign`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-unsign>.

- Drop the cryptographic signature from the working-copy commit:

`jj unsign`

- Drop the signature from a specific revision:

`jj unsign {{[-r|--revision]}} {{revset}}`

- Drop signatures from multiple revisions:

`jj unsign {{[-r|--revision]}} {{revset1}} {{[-r|--revision]}} {{revset2}}`
