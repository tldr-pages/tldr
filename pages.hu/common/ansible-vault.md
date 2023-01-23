# ansible-vault

> Titkosítja és dekódolja az értékeket, adatstruktúrákat és fájlokat az Ansible projektekben. További információ: <https://docs.ansible.com/ansible/latest/user_guide/vault.html#id17>.

- Új titkosított páncélteremfájl létrehozása jelszó megadásával:

`ansible-vault create {{vault_file}}`

- Új titkosított páncélteremfájl létrehozása egy páncélteremkulcsfájl titkosításával:

`ansible-vault create --vault-password-file={{password_file}} {{vault_file}}`

- Meglévő fájl titkosítása egy opcionális jelszófájl használatával:

`ansible-vault encrypt --vault-password-file={{password_file}} {{vault_file}}`

- Egy karakterlánc titkosítása az Ansible titkosított karakterlánc formátumának használatával, interaktív kérések megjelenítésével:

`ansible-vault encrypt_string`

- Titkosított fájl megtekintése jelszófájl használatával a visszafejtéshez:

`ansible-vault view --vault-password-file={{password_file}} {{vault_file}}`

- A már titkosított páncélteremfájl új jelszófájllal történő újbóli titkosítása:

`ansible-vault rekey --vault-password-file={{old_password_file}} --new-vault-password-file={{new_password_file}} {{vault_file}}`
