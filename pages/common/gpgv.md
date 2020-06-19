# gpgv

> Verify OpenPGP signatures.
> More information: <https://www.gnupg.org/documentation/manuals/gnupg/gpgv.html>.

- Verify a signed file.

`gpgv doc.txt`

- Verify a signed file using a detached signature.

`gpgv sigfile.asc doc.txt`

- Add a file to the list of keyrings (a single exported key also accounts as a keyring).

`gpgv --keyring ./alice.keyring sigfile.asc doc.txt`
