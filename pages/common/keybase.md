# keybase

> Key directory that maps social media identities to encryption keys in a publicly auditable manner.
> More information: <https://keybase.io/docs/command_line>.

- Follow another user:

`keybase follow {{username}}`

- Add a new proof:

`keybase prove {{service}} {{service_username}}`

- Sign a file:

`keybase sign --infile {{input_file}} --outfile {{output_file}}`

- Verify a signed file:

`keybase verify --infile {{input_file}} --outfile {{output_file}}`

- Encrypt a file:

`keybase encrypt --infile {{input_file}} --outfile {{output_file}} {{receiver}}`

- Decrypt a file:

`keybase decrypt --infile {{input_file}} --outfile {{output_file}}`

- Revoke current device, log out, and delete local data:

`keybase deprovision`
