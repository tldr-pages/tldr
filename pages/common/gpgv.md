# gpgv

> Verify OpenPGP signatures.
> See also: `gpg`.
> More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- Verify a clearsigned or inline-signed file (the signature is embedded in the file itself):

`gpgv {{path/to/file.asc}}`

- Verify a detached signature (`.asc` or `.sig`) against its corresponding data file:

`gpgv {{path/to/signature.asc}} {{path/to/data_file}}`

- Verify a detached signature using a specific public keyring or exported public key file (`.gpg` or `.kbx`):

`gpgv --keyring {{path/to/pubkey_or_keyring.gpg}} {{path/to/signature.asc}} {{path/to/data_file}}`

- Verify a detached signature using a specific public key file in plain text format (`.txt`):

`gpg --dearmor {{[-o|--output]}} {{path/to/pubkey.gpg}} < {{path/to/pubkey.txt}} && gpgv --keyring {{path/to/pubkey.gpg}} {{path/to/signature.asc}} {{path/to/data_file}}`
