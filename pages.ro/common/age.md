# age

> Un instrument simplu, modern și sigur de criptare a fișierelor.
> Mai multe informaţii: <https://age-encryption.org>

- Generați un fișier criptat care poate fi decriptat cu o frază de acces:

`age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`

- Generați o pereche de chei, salvând cheia privată într-un fișier necriptat și tipăriți cheia publică la stdout:

`age-keygen --output {{path/to/file}}`

- Criptați un fișier cu una sau mai multe chei publice care sunt introduse ca literale:

`age --recipient {{public_key_1}} --recipient {{public_key_2}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}`

- Criptați un fișier cu una sau mai multe chei publice care sunt specificate într-un fișier destinatar:

`age --recipients-file {{path/to/recipients_file}} {{path/to/unencrypted_file}} --output {{path/to/encrypted_file}}`

- Decripta un fișier cu o frază de acces:

`age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`

- Decripta un fișier cu un fișier cheie privată:

`age --decrypt --identity {{path/to/private_key_file}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`
