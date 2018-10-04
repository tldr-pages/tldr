# gpg-zip

> Encrypt files and directories in an archive using GPG.

- Encrypt a directory into archive.gpg using a passphrase:

`gpg-zip --symmetric --output {{archive.gpg}} {{dirname}}`

- Decrypt archive.gpg into a directory of the same name:

`gpg-zip --decrypt {{archive.gpg}}`

- List contents of the encrypted archive.gpg:

`gpg-zip --list-archive {{archive.gpg}}`
