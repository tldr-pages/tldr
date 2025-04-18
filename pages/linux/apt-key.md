# apt-key

> Key management utility for the APT Package Manager on Debian and Ubuntu.
> Note: `apt-key` is now deprecated (except for the use of `apt-key del` in maintainer scripts).
> More information: <https://manned.org/apt-key.8>.

- List trusted keys:

`apt-key list`

- Add a key to the trusted keystore:

`apt-key add {{public_key_file.asc}}`

- Delete a key from the trusted keystore:

`apt-key del {{key_id}}`

- Add a remote key to the trusted keystore:

`wget {{[-qO|--quiet --output-document]}} - {{https://host.tld/filename.key}} | apt-key add -`

- Add a key from keyserver with only key ID:

`apt-key adv --keyserver {{pgp.mit.edu}} --recv {{KEYID}}`
