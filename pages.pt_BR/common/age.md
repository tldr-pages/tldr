# age

> Uma simples, moderna e segura ferramenta de criptografia de arquivos.
> Veja também: `age-keygen` para geração de pares de chaves.
> Mais informações: <https://github.com/FiloSottile/age>.

- Gera um arquivo criptografado que pode ser descriptografado com uma frase-chave:

`age --passphrase --output {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Criptografa arquivo com uma ou mais chaves públicas que são inseridas como literais (repita o argumento `--recipient` para especificar múltiplas chaves públicas):

`age --recipient {{chave_pública}} --output {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Criptografa arquivo com um ou mais destinatários que são especificadas em um arquivo (um por linha):

`age --recipients-file {{caminho/para/arquivo_de_destinatários}} --output {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Descriptografa um arquivo com uma frase-chave:

`age --decrypt --output {{caminho/para/arquivo_descriptografado}} {{caminho/para/arquivo_criptografado}}`

- Descriptografa um arquivo com um arquivo de chave privada:

`age --decrypt --identity {{caminho/para/arquivo_de_chave_privada}} --output {{caminho/para/arquivo_descriptografado}} {{caminho/para/arquivo_criptografado}}`
