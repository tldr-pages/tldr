# gpg

> Gnu Privacy Guard

- sign doc.txt without encryption (writes output to doc.txt.asc)

`gpg --clearsign {{doc.txt}}`

- encrypt doc.txt for alice@example.com (output to doc.txt.gpg)

`gpg --encrypt --recipient {{alice@example.com}} {{doc.txt}}`

- encrypt doc.txt with only a passphrase (output to doc.txt.gpg)

`gpg --symmetric {{doc.txt}}`

- decrypt doc.txt.gpg (output to STDOUT)

`gpg --decrypt {{doc.txt.gpg}}`

- Import a public key

`gpg --import {{public.gpg}}`
