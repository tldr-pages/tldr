# chpasswd

> Change the passwords for multiple users by using stdin.
> More information: <https://manned.org/chpasswd.8>.

- Change the password for a specific user:

`printf "{{username}}:{{new_password}}" | sudo chpasswd`

- Change the passwords for multiple users (the input text must not contain any spaces):

`printf "{{username_1}}:{{new_password_1}}\n{{username_2}}:{{new_password_2}}" | sudo chpasswd`

- Change the password for a specific user, and specify it in encrypted form:

`printf "{{username}}:{{new_encrypted_password}}" | sudo chpasswd --encrypted`

- Change password for a user and use a specific cryptographic method to encrypt the password to be stored:

`printf "{{username}}:{{new_password}}" | sudo chpasswd --crypt-method {{NONE|DES|MD5|SHA256|SHA512}}`
