# ansible-vault

> Criptează și decriptează valorile, structurile de date și fișierele din cadrul proiectelor Ansible.
> Mai multe informaţii: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>

- Creați un nou fișier criptat cu un prompt pentru o parolă:

`ansible-vault create {{vault_file}}`

- Creați un nou fișier criptat cu ajutorul unui fișier cheie seif pentru a-l cripta:

`ansible-vault create --vault-password-file={{password_file}} {{vault_file}}`

- Criptați un fișier existent utilizând un fișier cu parolă opțional:

`ansible-vault encrypt --vault-password-file={{password_file}} {{vault_file}}`

- Criptați un șir utilizând formatul șir criptat al Ansible, afișând solicitări interactive:

`ansible-vault encrypt_string`

- Vizualizați un fișier criptat, folosind un fișier parolă pentru a decripta:

`ansible-vault view --vault-password-file={{password_file}} {{vault_file}}`

- Re-cheie deja criptat fișier seif cu un nou fișier parolă:

`ansible-vault rekey --vault-password-file={{old_password_file}} --new-vault-password-file={{new_password_file}} {{vault_file}}`
