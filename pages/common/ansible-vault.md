# ansible-vault

> Encrypts & decrypts values, data structures and files within Ansible projects.
> More information: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Create a new encrypted vault file with a prompt for a password:

`ansible-vault create {{path/to/file}}`

- Create a new encrypted vault file using a vault key file to encrypt it:

`ansible-vault create --vault-password-file={{path/to/file}} {{path/to/file}}`

- Encrypt an existing file using an optional password file:

`ansible-vault encrypt --vault-password-file={{path/to/file}} {{path/to/file}}`

- Encrypt a string using Ansible's encrypted string format, displaying interactive prompts:

`ansible-vault encrypt_string`

- View an encrypted file, using a password file to decrypt:

`ansible-vault view --vault-password-file={{path/to/file}} {{path/to/file}}`

- Re-key already encrypted vault file with a new password file:

`ansible-vault rekey --vault-password-file={{path/to/file}} --new-vault-password-file={{path/to/file}} {{path/to/file}}`
