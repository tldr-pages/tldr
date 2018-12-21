# apt-key

> Key management utility for the APT Package Manager on Debian and Ubuntu.

- List trusted keys:

`apt-key list`

- Add a key to the trusted keystore:

`apt-key add {{public_key_file.asc}}`

- Delete a key from the trusted keystore:

`apt-key del {{key_id}}`

- Add a remote key to the trusted keystore:

`wget -qO - {{https://host.tld/filename.key}} | apt-key add -`

- Add a key from keyserver with only key id:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
