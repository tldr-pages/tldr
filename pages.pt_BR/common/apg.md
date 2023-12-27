# apg

> Criar senhas aleatórias arbitrariamente complexas.
> Mais informações: <https://manned.org/apg>.

- Cria senha aleatória (tamanho padrão para as senhas é 8 caracteres):

`apg`

- Cria senha com pelo menos 1 símbolo (S), 1 número (N), 1 letra maiúscula (C), 1 letra minúscula (L):

`apg -M SNCL`

- Cria uma senha com 16 caracteres:

`apg -m {{16}}`

- Cria senha com tamanho máximo de 16 caracteres:

`apg -x {{16}}`

- Cria uma senha que não aparece em um dicionário provido pelo usuário:

`apg -r {{caminho/para/arquivo_de_dicionario}}`
