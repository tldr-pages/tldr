# jj sign

> Cryptographically sign revisions.
> Requires configuring a commit signing backend.
> See also: `jj unsign`.
> More information: <https://docs.jj-vcs.dev/latest/cli-reference/#jj-sign>.

- Sign revisions configured by the `revsets.sign` setting:

`jj sign`

- Sign a specific revision:

`jj sign {{[-r|--revision]}} {{revset}}`

- Sign multiple revisions:

`jj sign {{[-r|--revision]}} {{revset1}} {{[-r|--revision]}} {{revset2}}`

- Sign revisions using a specific signing key:

`jj sign --key {{key_id}} {{[-r|--revision]}} {{revset}}`
