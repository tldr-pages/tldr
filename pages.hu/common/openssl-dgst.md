# openssl dgst

> OpenSSL parancs az emésztési értékek létrehozására és aláírási műveletek végrehajtására. További információ: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>.

- Kiszámítja az SHA256 digestet egy fájlhoz, és az eredményt egy adott fájlba menti:

`openssl dgst -sha256 -binary -out {{output_file}} {{input_file}}`

- Egy fájl aláírása RSA-kulcs használatával, az eredmény mentése egy adott fájlba:

`openssl dgst -sign {{private_key_file}} -sha256 -sigopt rsa_padding_mode:pss -out {{output_file}} {{input_file}}`

- RSA aláírás ellenőrzése:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} -sigopt rsa_padding_mode:pss {{signature_message_file}}`

- Fájl aláírása ECDSA kulcs használatával:

`openssl dgst -sign {{private_key_file}} -sha256 -out {{output_file}} {{input_file}}`

- ECDSA aláírás ellenőrzése:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} {{signature_message_file}}`
