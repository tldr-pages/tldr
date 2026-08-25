# ansible-vault

> Cifra e decifra valori, strutture dati e file nei progetti Ansible.
> Maggiori informazioni: <https://docs.ansible.com/projects/ansible/latest/vault_guide/index.html>.

- Crea un nuovo file vault crittografato con richiesta interattiva della password:

`ansible-vault create {{percorso/al/vault_file}}`

- Modifica, visualizza o ricifra (re-encrypt) un file vault crittografato esistente con richiesta della password:

`ansible-vault {{edit|view|rekey}} {{percorso/al/vault_file}}`

- Crea un nuovo file vault crittografato usando un file password per la cifratura:

`ansible-vault create --vault-password-file {{percorso/al/password_file}} {{percorso/al/vault_file}}`

- Cifra un file plaintext esistente sul posto usando un file password:

`ansible-vault encrypt --vault-password-file {{percorso/al/password_file}} {{percorso/al/file}}`

- Cifra una stringa usando il formato stringa crittografata di Ansible con prompt interattivi:

`ansible-vault encrypt_string`

- Visualizza un file vault crittografato usando un file password per la decifratura:

`ansible-vault view --vault-password-file {{percorso/al/password_file}} {{percorso/al/vault_file}}`

- Ricifra (re-encrypt) un file vault già crittografato con un nuovo file password:

`ansible-vault rekey --vault-password-file {{percorso/al/vecchio_password_file}} --new-vault-password-file {{percorso/al/nuovo_password_file}} {{percorso/al/vault_file}}`
