# strings

> Procura strings imprimíveis em um arquivo objeto ou binário.
> Mais informações: <https://manned.org/strings>.

- Imprime todas as strings em um binário:

`strings {{caminho/para/arquivo}}`

- Limita resultados a strings com pelo menos n caracteres:

`strings {{[-n|--bytes]}} {{n}} {{caminho/para/arquivo}}`

- Prefixa cada resultado com seu deslocamento dentro do arquivo:

`strings {{[-t|--radix]}} d {{caminho/para/arquivo}}`

- Prefixa cada resultado com seu deslocamento dentro do arquivo em hexadecimal:

`strings {{[-t|--radix]}} x {{caminho/para/arquivo}}`
