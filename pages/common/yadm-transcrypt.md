# yadm-transcrypt

> If transcrypt is installed, this command allows you to pass options directly to transcrypt.
> With the environment configured to use the yadm repository.
> Transcrypt enables transparent encryption and decryption of files in a git repository.
> You can read <https://github.com/elasticdog/transcrypt> for details.

- To set the symmetric cipher to utilize for encryption:

`yadm  transcrypt --cipher={{cipher}}`

- To pass the password to derive the key from:

`yadm transcrypt --password={{password}}`

- To assume yes and accept defaults for non-specified options:

`yadm transcrypt --yes`

- To display the current repository's cipher and password:

`yadm transcrypt --display`

- To re-encrypt all encrypted files using new credentials:

`yadm transcrypt --rekey`
