# ansible-vault

> Encrypts & decrypts values, data structures and files within Ansible projects.
> More information: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.


- Create a new encrypted vault file with vault prompt for password:

`ansible-vault create {{vault_file}}`

- Create a new encrypted vault file with vault key file to encrypt with:

`ansible-vault create --vault-password-file={{password_file}} {{vault_file}}`

- Encrypt existing file, using password file (optional):

`ansible-vault encrypt --vault-password-file={{password_file}} {{vault_file}}`

- Encrypt a string using ansible's encrypted string format using prompts:

`ansible-vault encrypt_string` 

- View an encrypted file, using password file to decrypt:

`ansible-vault view --vault-password-file={{password_file}} {{vault_file}}`

- Rekey already encrypted vault file with new password file:

`ansible-vault rekey --vault-password-file={{old_password_file}} --new-vault-password-file={{new_password_file}} {{vault_file}}`

