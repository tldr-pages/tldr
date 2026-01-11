# ansible-vault

> Cifra e decifra valori, strutture dati e file nei progetti Ansible.
> Maggiori informazioni: <https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>.

- Crea un nuovo file vault cifrato con richiesta interattiva della password:

`ansible-vault create {{file_vault}}`

- Crea un nuovo file vault cifrato usando un file chiave vault per la cifratura:

`ansible-vault create --vault-password-file {{file_password}} {{file_vault}}`

- Cifra un file esistente usando un file password opzionale:

`ansible-vault encrypt --vault-password-file {{file_password}} {{file_vault}}`

- Cifra una stringa usando il formato stringa cifrata di Ansible, con prompt interattivi:

`ansible-vault encrypt_string`

- Visualizza un file cifrato, usando un file password per la decifratura:

`ansible-vault view --vault-password-file {{file_password}} {{file_vault}}`

- Ricifra un file vault già cifrato con un nuovo file password:

`ansible-vault rekey --vault-password-file {{vecchio_file_password}} --new-vault-password-file {{nuovo_file_password}} {{file_vault}}`
