# gpg

> Encryption and signing tool

- generate key

`gpg --gen-key`

- generate revoke cert

`gpg --gen-revoke {{user_id}}`

- list keys

`gpg --list-keys`

- delete key

`gpg --delete-key {{user_id}}`

- print key in ascii

`gpg --armor --output {{output_file}} --export {{user_id}}`
`gpg --armor --output {{output_file}} --export-secret-keys`

- upload publich key to server

`gpg --send-keys --keyserver {{key_server}}`

- generate publich key fingerprint

`gpg --fingerprint {{user_id}}`

- encrypt

`gpg --recipient {{user_id}} --output {{output_file}} --encrypt {{input_file}}`

- decrypt

`gpg --decrypt {{input_file}} --output {{output_file}}`
`gpg {{input_file}}`

- sign document

`gpg --sign {{input_file}}`
`gpg --clearsign {{input_file}}`
`gpg --detach-sign {{input_file}}`
`gpg --armor --detach-sign {{input_file}}`

- verify sign

`gpg --verify {{input_file}}`

- encrypt and sign

`gpg --local-user {{local_user_id}} --recipient {{remote_user_id}} --armor --sign --encrypt {{input_file}}`
