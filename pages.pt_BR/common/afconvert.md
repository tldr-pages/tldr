# afconvert

> Converte entre os formatos de arquivo AFF e Raw.
> Mais informações: <https://manned.org/afconvert.1>.

- Usa uma extensão específica (padrão: `aff`):

`afconvert -a {{extensão}} {{caminho/para/arquivo_de_entrada}} {{caminho/para/arquivo_de_saida1 caminho/para/arquivo_de_saida2 ...}}`

- Usa um nível específico de compressão (padrão: `7`):

`afconvert -X{{0..7}} {{caminho/para/arquivo_de_entrada}} {{caminho/para/arquivo_de_saida1 caminho/para/arquivo_de_saida2 ...}}`
