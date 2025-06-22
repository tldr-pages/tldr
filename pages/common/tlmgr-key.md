# tlmgr key

> Manage GPG keys used to verify TeX Live databases.
> More information: <https://www.tug.org/texlive/doc/tlmgr.html#key>.

- List all keys for TeX Live:

`tlmgr key list`

- Add a key from a specific file:

`sudo tlmgr key add {{path/to/key.gpg}}`

- Add a key from `stdin`:

`sudo tlmgr key add - < {{path/to/key.gpg}}`

- Remove a specific key by its ID:

`sudo tlmgr key remove {{key_id}}`
