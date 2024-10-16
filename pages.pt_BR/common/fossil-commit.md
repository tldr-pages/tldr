# fossil commit

> Faz commit de arquivos para um repositório Fossil.
> Mais informações: <https://fossil-scm.org/home/help/commit>.

- Cria uma nova versão contendo todas as alterações no checkout atual; o usuário será solicitado a inserir um comentário:

`fossil commit`

- Cria uma nova versão contendo todas as alterações no checkout atual, usando o comentário especificado:

`fossil commit --comment "{{comentário}}"`

- Cria uma nova versão contendo todas as alterações no checkout atual com um comentário lido de um arquivo específico:

`fossil commit --message-file {{caminho/para/arquivos_de_mensagem_de_commit}}`

- Cria uma nova versão contendo alterações dos arquivos especificados; o usuário será solicitado a fornecer um comentário:

`fossil commit {{caminho/para/arquivo1 caminho/para/arquivo2 ...}}`
