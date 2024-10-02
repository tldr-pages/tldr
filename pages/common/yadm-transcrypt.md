# yadm-transcrypt

> If `transcrypt` is installed, this command allows you to pass options directly to `transcrypt`.
> With the environment configured to use the yadm repository.
> Transcrypt enables transparent encryption and decryption of files in a Git repository.
> More information: <https://github.com/elasticdog/transcrypt>.

- Set the symmetric cipher to utilize for encryption:

`yadm transcrypt --cipher={{cipher}}`

- Pass the password to derive the key from:

`yadm transcrypt --password={{password}}`

- Assume yes and accept defaults for non-specified options:

`yadm transcrypt --yes`

- Display the current repository's cipher and password:

`yadm transcrypt --display`

- Re -encrypt all encrypted files using new credentials:

`yadm transcrypt --rekey`
