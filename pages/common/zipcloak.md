# zipcloak

> Encrypt the contents within a Zip archive.
> More information: <https://manned.org/zipcloak>.

- Encrypt the contents of a Zip archive:

`zipcloak {{path/to/archive.zip}}`

- Decrypt the contents of a Zip archive:

`zipcloak {{[-d|--decrypt]}} {{path/to/archive.zip}}`

- Output the encrypted contents into a new Zip archive:

`zipcloak {{path/to/archive.zip}} {{[-O|--output-file]}} {{path/to/encrypted.zip}}`
