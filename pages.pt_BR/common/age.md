# age

> Uma simples, moderna e segura ferramenta de criptografia de arquivos.
> Veja também: `age-keygen`.
> Mais informações: <https://github.com/FiloSottile/age#usage>.

- Gera um arquivo criptografado que pode ser descriptografado com uma frase-chave:

`age {{[-p|--passphrase]}} {{[-o|--output]}} {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Criptografa arquivo com uma ou mais chaves públicas que são inseridas como literais (repita o argumento `--recipient` para especificar múltiplas chaves públicas):

`age {{[-r|--recipient]}} {{chave_pública}} {{[-o|--output]}} {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Criptografa arquivo com um ou mais destinatários que são especificadas em um arquivo (um por linha):

`age {{[-R|--recipients-file]}} {{caminho/para/arquivo_de_destinatários}} {{[-o|--output]}} {{caminho/para/arquivo_criptografado}} {{caminho/para/arquivo_descriptografado}}`

- Descriptografa um arquivo com uma frase-chave:

`age {{[-d|--decrypt]}} {{[-o|--output]}} {{caminho/para/arquivo_descriptografado}} {{caminho/para/arquivo_criptografado}}`

- Descriptografa um arquivo com um arquivo de chave privada:

`age {{[-d|--decrypt]}} {{[-i|--identity]}} {{caminho/para/arquivo_de_chave_privada}} {{[-o|--output]}} {{caminho/para/arquivo_descriptografado}} {{caminho/para/arquivo_criptografado}}`
