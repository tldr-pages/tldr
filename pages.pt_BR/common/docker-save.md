# docker save

> Exportar uma ou mais imagens do Docker para um arquivo de arquivamento.
> Mais informações: <https://docs.docker.com/reference/cli/docker/image/save/>.

- Salva uma imagem redirecionando `stdout` para um arquivo tar:

`docker save {{imagem}}:{{tag}} > {{caminho/para/arquivo.tar}}`

- Salva uma imagem em um arquivo tar:

`docker save {{[-o|--output]}} {{caminho/para/arquivo.tar}} {{imagem}}:{{tag}}`

- Salva todas as tags da imagem:

`docker save {{[-o|--output]}} {{caminho/para/arquivo.tar}} {{nome_da_imagem}}`

- Seleciona tags específicas de uma imagem para salvar:

`docker save {{[-o|--output]}} {{caminho/para/arquivo.tar}} {{nome_da_imagem:tag1 nome_da_imagem:tag2 ...}}`
