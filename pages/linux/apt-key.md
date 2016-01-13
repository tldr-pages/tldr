# apt-key

> Key management utility for the APT Package Manager on Debian and Ubuntu.

- List trusted key:

`apt-key list`

- Add a key to the trusted keystor:

`apt-key add {{public_key_file.asc}}`

- Delete a key from the trusted keystor:

`apt-key del {{key_id}}`

- Add a remote key to the trusted keystor:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`
