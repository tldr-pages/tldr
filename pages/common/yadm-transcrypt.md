# yadm transcrypt

> If `transcrypt` is installed, this command allows you to pass options directly to `transcrypt`.
> With the environment configured to use the yadm repository.
> Transcrypt enables transparent encryption and decryption of files in a Git repository.
> More information: <https://github.com/elasticdog/transcrypt#command-line-options>.

- Set the symmetric cipher to utilize for encryption:

`yadm transcrypt {{[-c|--cipher]}} {{cipher}}`

- Pass the password to derive the key from:

`yadm transcrypt {{[-p|--password]}} {{password}}`

- Assume yes and accept defaults for non-specified options:

`yadm transcrypt {{[-y|--yes]}}`

- Display the current repository's cipher and password:

`yadm transcrypt {{[-d|--display]}}`

- Re -encrypt all encrypted files using new credentials:

`yadm transcrypt {{[-r|--rekey]}}`
