# ansible-vault

> Verschlüsselt und entschlüsselt Werte, Datenstrukturen und Dateien innerhalb von Ansible-Projekten.
> Mehr Informationen: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Erstellen Sie eine neue verschlüsselte Vault Datei mit einer Eingabeaufforderung für ein Passwort:

`ansible-vault create {{vault_file}}`

- Erstellen Sie eine neue verschlüsselte Vault Datei mit einer Vault-Schlüsseldatei, um sie zu verschlüsseln:

`ansible-vault create --vault-password-file={{password_file}} {{vault_file}}`

- Verschlüsseln Sie eine vorhandene Datei mit einer optionalen Kennwortdatei:

`ansible-vault verschlüsseln --vault-password-file={{password_file}} {{vault_file}}`

- Verschlüsseln Sie eine Zeichenfolge mit dem verschlüsselten Zeichenfolgenformat von Ansible, wobei interaktive Eingabeaufforderungen angezeigt werden:

`ansible-vault verschlüsseln_zeichenkette`

- Anzeigen einer verschlüsselten Datei, wobei eine Kennwortdatei zum Entschlüsseln verwendet wird:

`ansible-vault view --vault-password-file={{password_file}} {{vault_file}}`

- Verschlüsseln Sie eine bereits verschlüsselte Vault Datei mit einer neuen Kennwortdatei neu:

`ansible-vault rekey --vault-password-file={{old_password_file}} --new-vault-password-file={{new_password_file}} {{vault_file}}`
