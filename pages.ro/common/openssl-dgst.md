# openssl dgst

> comanda OpenSSL pentru a genera valori de digerare și a efectua operații de semnătură.
> Mai multe informaţii: <https://www.openssl.org/docs/manmaster/man1/openssl-dgst.html>

- Calculați digest-ul SHA256 pentru un fișier, salvând rezultatul într-un anumit fișier:

`openssl dgst -sha256 -binary -out {{output_file}} {{input_file}}`

- Semnați un fișier utilizând o cheie RSA, salvând rezultatul într-un anumit fișier:

`openssl dgst -sign {{private_key_file}} -sha256 -sigopt rsa_padding_mode:pss -out {{output_file}} {{input_file}}`

- Verificați o semnătură RSA:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} -sigopt rsa_padding_mode:pss {{signature_message_file}}`

- Semnează un fișier utilizând și cheia ECDSA:

`openssl dgst -sign {{private_key_file}} -sha256 -out {{output_file}} {{input_file}}`

- Verificați o semnătură ECDSA:

`openssl dgst -verify {{public_key_file}} -signature {{signature_file}} {{signature_message_file}}`
