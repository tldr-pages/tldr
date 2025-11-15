# gh gpg-key

> Manage GPG keys registered with the authorized GitHub account.
> See also: `gpg`.
> More information: <https://cli.github.com/manual/gh_gpg-key>.

- List GPG keys in the authorized GitHub account:

`gh gpg-key {{[ls|list]}}`

- Add a GPG key to the authorized GitHub account by specifying the key file:

`gh gpg-key add {{path/to/key_file}}`

- Add a GPG key to the authorized GitHub account by specifying the key ID:

`gpg {{[-a|--armor]}} --export {{key_id}} | gh gpg-key add -`

- Delete a GPG key from the authorized GitHub account:

`gh gpg-key delete {{key_id}}`
