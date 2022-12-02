# keybase

> Key directory that maps social media identities to encryption keys in a publicly auditable manner.
> More information: <https://keybase.io/docs/command_line>.

- Follow another user:

`keybase follow {{username}}`

- Add a new proof:

`keybase prove {{service}} {{service_username}}`

- Sign a file:

`keybase sign --infile {{path/to/file}} --outfile {{path/to/file}}`

- Verify a signed file:

`keybase verify --infile {{path/to/file}} --outfile {{path/to/file}}`

- Encrypt a file:

`keybase encrypt --infile {{path/to/file}} --outfile {{path/to/file}} {{receiver}}`

- Decrypt a file:

`keybase decrypt --infile {{path/to/file}} --outfile {{path/to/file}}`

- Revoke current device, log out, and delete local data:

`keybase deprovision`
