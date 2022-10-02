# certutil

> Manage keys and certificate in both NSS databases and other NSS tokens.
> More information: <https://manpages.ubuntu.com/manpages/xenial/man1/certutil.1.html>.

- Create a new certificate database:

`certutil -N -d .`

- List all certificates in a database:

`certutil -L -d .`

- List all private keys in a database:

`certutil -K -d . -f pwdfile.txt`

- Import the signed certificate into the requesters database:

`certutil -A -n "Server-cert" -t ",," -i server.crt -d .`

- To add subject alternative names, use a comma separated list with the option -8 IE:

`certutil -S -f pwdfile.txt -d . -t ",," -c "Server-Cert" -n "server1" -g 2048 -s "CN=testuser1,O=testrelm.test"`
