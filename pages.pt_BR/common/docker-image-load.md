# docker load

> Carregar imagens do Docker a partir de arquivos ou `stdin`.
> Mais informações: <https://docs.docker.com/reference/cli/docker/image/load/>.

- Carrega uma imagem do Docker a partir do `stdin`:

`docker load < {{caminho/para/arquivo_imagem.tar}}`

- Carrega uma imagem do Docker a partir de um arquivo específico:

`docker load {{[-i|--input]}} {{caminho/para/arquivo_imagem.tar}}`

- Carrega uma imagem do Docker a partir de um arquivo específico no modo silencioso:

`docker load {{[-q|--quiet]}} {{[-i|--input]}} {{caminho/para/arquivo_imagem.tar}}`
