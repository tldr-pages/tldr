# gpg

> Gnu Privacy Guard.

- Create a key

`gpg --gen-key`

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

- To list the keys in your public key ring:

`gpg --list-keys`

- To list the keys in your secret key ring:

`gpg --list-secret-keys`

- To generate a short list of numbers that you can use via an alternative method to verify a public key, use:

`gpg --fingerprint > fingerprint`
