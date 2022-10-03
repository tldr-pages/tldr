# certutil

> Manage keys and certificates in both NSS databases and other NSS tokens.
> More information: <https://manned.org/certutil>.

- Create a new certificate database:

`certutil -N -d .`

- List all certificates in a database:

`certutil -L -d .`

- List all private keys in a database:

`certutil -K -d . -f {{path/to/pwdfile.txt}}`

- Import the signed certificate into the requesters database:

`certutil -A -n "Server-cert" -t ",," -i {{path/to/file.crt}} -d .`

- Add subject alternative names to a given certificate:

`certutil -S -f pwdfile.txt -d . -t ",," -c "Server-Cert" -n "server1" -g 2048 -s "CN=testuser1,O=testrelm.test"`
