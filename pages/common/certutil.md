# certutil

> Manage keys and certificates in both NSS databases and other NSS tokens.
> More information: <https://manned.org/certutil>.

- Create a new certificate database:

`certutil -N -d .`

- List all certificates in a database:

`certutil -L -d .`

- List all private keys in a database:

`certutil -K -d . -f {{path/to/password_file.txt}}`

- Import the signed certificate into the requesters database:

`certutil -A -n "{{server_certificate}}" -t ",," -i {{path/to/file.crt}} -d .`

- Add subject alternative names to a given certificate:

`certutil -S -f {{path/to/password_file.txt}} -d . -t ",," -c "{{server_certificate}}" -n "{{server_name}}" -g {{2048}} -s "CN={{common_name}},O={{organization}}"`
