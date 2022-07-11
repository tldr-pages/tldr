# tlmgr key

> Manage GPG keys used to verify TeX Live databases.
> More information: <https://www.tug.org/texlive/tlmgr.html>.

- List all keys for TeX Live:

`tlmgr key list`

- Add a key from a specific file:

`sudo tlmgr key add {{path/to/key.gpg}}`

- Add a key from stdin:

`cat {{path/to/key.gpg}} | sudo tlmgr key add -`

- Remove a specific key by its ID:

`sudo tlmgr key remove {{key_id}}`
