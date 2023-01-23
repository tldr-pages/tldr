# age

> Egy egyszerű, modern és biztonságos fájltitkosító eszköz. További információ: <https://age-encryption.org>.

- Titkosított fájl generálása, amely egy jelszóval visszafejthető:

`age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Generáljon kulcspárt, a titkos kulcsot mentse el egy titkosítatlan fájlba, a nyilvános kulcsot pedig nyomtassa ki a `stdout` címre:

`age-keygen --output {{path/to/file}}`

- Egy fájl titkosítása egy vagy több, literálként megadott nyilvános kulccsal:

`age --recipient {{public_key_1}} --recipient {{public_key_2}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}`

- Egy fájl titkosítása egy vagy több nyilvános kulccsal, amelyek egy címzett fájlban vannak megadva:

`age --recipients-file {{path/to/recipients_file}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}`

- Egy fájl visszafejtése egy jelszóval:

`age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`

- Fájl visszafejtése titkos kulcsfájllal:

`age --decrypt --identity {{path/to/private_key_file}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`
