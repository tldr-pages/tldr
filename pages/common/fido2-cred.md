# fido2-cred

> Create and verify fido2.x key credentials.
> More information: <https://man.archlinux.org/man/fido2-cred.1.en>
> See also: <https://man.archlinux.org/man/fido2-token.1.en>
>           <https://manpages.debian.org/unstable/yubikey-manager/ykman.1.en.html>

- Add a non-resident key (key unrecoverable without saving output):

```
 read -rs pass < /dev/tty > key.pem
 fido2-cred -M -c3 -t uv=true -t pin=true -r "$auth_device" <<EOF
 $(printf "%s" "$pass" | openssl sha256 -binary | base64)
 example.com
 username
 $(dd if=/dev/urandom bs=1 count=32 status=none | base64)
 EOF

 ```

- Add a resident password with user verification required on
  write (`-t`) and read (`-c3`) (better off using `ykman`):

```
read -rs pass < /dev/tty
fido2-cred -M -c3 -t uv=true -t pin=true -r "$auth_device" <<EOF
$(printf "%s" "$pass" | openssl sha256 -binary | base64)
example.com
username
$(dd if=/dev/urandom bs=1 count=32 status=none | base64)
EOF

```

- Verify a key

`fido2-cred -V -r -c 3 < key.pem`
