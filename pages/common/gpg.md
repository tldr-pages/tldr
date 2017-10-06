# gpg

> GNU Privacy Guard.

- Sign doc.txt without encryption (writes output to doc.txt.asc):

`gpg --clearsign {{doc.txt}}`

- Encrypt doc.txt for alice@example.com (output to doc.txt.gpg):

`gpg --encrypt --recipient {{alice@example.com}} {{doc.txt}}`

- Encrypt doc.txt with only a passphrase (output to doc.txt.gpg):

`gpg --symmetric {{doc.txt}}`

- Decrypt doc.txt.gpg (output to STDOUT):

`gpg --decrypt {{doc.txt.gpg}}`

- Import a public key:

`gpg --import {{public.gpg}}`

- Export public key for alice@example.com (output to STDOUT):

`gpg --export --armor {{alice@example.com}}`

- Export private key for alice@example.com (output to STDOUT):

`gpg --export-secret-keys --armor {{alice@example.com}}`
