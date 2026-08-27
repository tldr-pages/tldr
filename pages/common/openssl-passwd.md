# openssl passwd

> Generate password hash.
> More information: <https://docs.openssl.org/master/man1/openssl-passwd/>.

- Generate password hash in SHA256 algorithm (Linux only):

`openssl passwd -5`

- Generate password hash in APR1 algorithm:

`openssl passwd -apr1`

- Generate password hash in APR1 algorithm with salt:

`openssl passwd -apr1 -salt {{salt_string}}`

- Generate password hash in APR1 and display the password and the hash:

`openssl passwd -apr1 -table`

- Generate password hash from `stdin`:

`echo -n "{{password}}" | openssl passwd {{-apr1}} -stdin`
