# openssl passwd

> Generate password hash.
> More information: <https://docs.openssl.org/master/man1/openssl-passwd/>.

- Generate password hash in MD5 based BSD password algorithm:

`openssl passwd -1`

- Generate password hash in apr1 algorithm:

`openssl passwd -apr1`

- Generate password hash in apr1 algorithm with salt:

`openssl passwd -apr1 -salt {{salt_string}}`

- Generate password hash in apr1 and display the password and the hash:

`openssl passwd -apr1 -table`

- Generate password hash from `stdin`:

`echo -n "{{password}}" | openssl passwd -apr1 -stdin`
