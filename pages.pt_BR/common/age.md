age

>Uma ferramenta simples, moderna e segura de criptografia de arquivos. Veja também: age-keygen para gerar pares de chaves. Mais informações: https://github.com/FiloSottile/age.



Gerar um arquivo criptografado que pode ser descriptografado com uma senha:



`age --passphrase --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`


Criptografar um arquivo com uma ou mais chaves públicas inseridas como literais (repita a flag --recipient para especificar várias chaves públicas):

`age --recipient {{public_key}} --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`




Criptografar um arquivo para um ou mais destinatários cujas chaves públicas estão especificadas em um arquivo (uma por linha):

`age --recipients-file {{path/to/recipients_file}} --output {{path/to/encrypted_file}} {{path/to/unencrypted_file}}`


Descriptografar um arquivo com uma senha:

`age --decrypt --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`


Descriptografar um arquivo com um arquivo de chave privada:


`age --decrypt --identity {{path/to/private_key_file}} --output {{path/to/decrypted_file}} {{path/to/encrypted_file}}`
