# ansible-vault

> Verschlüsselt und entschlüsselt Werte, Datenstrukturen und Dateien innerhalb von Ansible-Projekten.
> Weitere Informationen: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Erstelle eine neue verschlüsselte Vault-Datei mit einer Eingabeaufforderung für ein Passwort:

`ansible-vault create {{vault_datei}}`

- Erstelle eine neue verschlüsselte Vault-Datei mit einer Vault-Schlüsseldatei, um sie zu verschlüsseln:

`ansible-vault create --vault-password-file {{schlüsseldatei}} {{vault_datei}}`

- Verschlüssle eine vorhandene Datei mit einer optionalen Schlüsseldatei:

`ansible-vault encrypt --vault-password-file {{schlüsseldatei}} {{vault_file}}`

- Verschlüssle eine Zeichenfolge mit dem verschlüsselten Zeichenfolgenformat von Ansible, wobei interaktive Eingabeaufforderungen angezeigt werden:

`ansible-vault encrypt_string`

- Zeige eine verschlüsselte Datei an, wobei eine Kennwortdatei zum Entschlüsseln verwendet wird:

`ansible-vault view --vault-password-file {{schlüsseldatei}} {{vault_datei}}`

- Verschlüssle eine bereits verschlüsselte Vault Datei mit einer neuen Kennwortdatei neu:

`ansible-vault rekey --vault-password-file {{alte_schlüsseldatei}} --new-vault-password-file {{neue_schlüsseldatei}} {{vault_datei}}`
