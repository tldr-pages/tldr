# keybase

> Key directory that maps social media identities to encryption keys in a publicly auditable manner.
> More information: <https://book.keybase.io/docs/cli>.

- Follow another user:

`keybase follow {{username}}`

- Add a new proof:

`keybase prove {{service}} {{service_username}}`

- Sign a file:

`keybase sign {{[-i|--infile]}} {{input_file}} {{[-o|--outfile]}} {{output_file}}`

- Verify a signed file:

`keybase verify {{[-i|--infile]}} {{input_file}} {{[-o|--outfile]}} {{output_file}}`

- Encrypt a file:

`keybase encrypt {{[-i|--infile]}} {{input_file}} {{[-o|--outfile]}} {{output_file}} {{receiver}}`

- Decrypt a file:

`keybase decrypt {{[-i|--infile]}} {{input_file}} {{[-o|--outfile]}} {{output_file}}`

- Revoke current device, log out, and delete local data:

`keybase deprovision`
