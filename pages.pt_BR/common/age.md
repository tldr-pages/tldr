# age

> Uma simples, moderna e segura ferramenta de criptografia de arquivos.
> Mais informações: <https://age-encryption.org>.

- Gera um arquivo criptografado que pode ser descriptografado com uma frase-chave:

`age --passphrase --output {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Gera um par de chaves, salvando a chave privada em um arquivo não criptografado e imprimindo a chave pública para `stdout`:

`age-keygen --output {{caminho/para/arquivo}}`

- Criptografa arquivo com uma ou mais chaves públicas que são inseridas como literais:

`age --recipient {{chave_pública_1}} --recipient {{chave_pública_2}} {{caminho/para/arquivo_descriptografado}} --output {{caminho/para/arquivo_criptografado}}`

- Criptografa arquivo com uma ou mais chaves públicas que são especificadas no arquivo do destinatário:

`age --recipients-file {{caminho/para/arquivo_destinatário}} {{caminho/para/arquivo_descriptografado}} --output {{caminho/para/arquivo_criptografado}}`

- Descriptografa um arquivo com uma frase-chave:

`age --decrypt --output {{caminho/para/arquivo_descriptografado}} {{caminho/para/arquivo_criptografado}}`

- Descriptografa um arquivo com um arquivo chave privada:

`age --decrypt --identity {{caminho/para/arquivo_chave_privada}} --output {{caminho/para/arquivo_descriptografado}} {{caminho/para/arquivo_criptografado}}`
