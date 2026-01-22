# sq

> A modern OpenPGP command-line tool.
> See also: `gpg`.
> More information: <https://sequoia-pgp.gitlab.io/sequoia-sq/man/sq.1.html>.

- Encrypt a file using a password (symmetric encryption):

`sq encrypt --with-password --without-signature {{path/to/file}} --output {{path/to/file.pgp}}`

- Decrypt a password-protected file:

`sq decrypt {{path/to/file.pgp}} --output {{path/to/file}}`

- Inspect an OpenPGP file to see its metadata and structure:

`sq inspect {{path/to/file.pgp}}`

- Verify a file with a detached signature and a certificate file:

`sq verify --signer-file {{path/to/signer.asc}} --signature-file {{path/to/file.sig}} {{path/to/file}}`

- Verify a file with an embedded (cleartext) signature and a certificate file:

`sq verify --signer-file {{path/to/signer.asc}} --cleartext {{path/to/file}}`

- Generate own key, and save it on the local key store:

`sq key generate --own-key --name {{Name}} --email {{name@example.com}}`

- List all secret keys or certs managed by the local key store:

`sq {{key|cert}} list`

- List current configuration and storage paths:

`sq config inspect paths`
