# chpasswd

> Change passwords for multiple users via taking input from stdin.
> More information: <https://manpages.debian.org/jessie/passwd/chpasswd.8.en.html>.

- Change password for a user.

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- Change passwords for multiple users (Mind the lack of space in the stdin text).

`printf "{{username_one}}:{{new_password_one}}\n{{username_two}}:{{new_password_two}}" | sudo chpasswd`

- Change password into the supplied encrypted password for a user.

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd --encrypted`

- Change password for a user and use a specific cryptographic method to encrypt the password to be stored.

`printf "{{username}}:{{new_password}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}` 