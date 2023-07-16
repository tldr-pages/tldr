# docker load

> Carregar imagens do Docker a partir de arquivos ou `stdin`.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/load/>.

- Carregar uma imagem do Docker a partir do `stdin`:

`docker load < {{caminho/para/arquivo_imagem.tar}}`

- Carregar uma imagem do Docker a partir de um arquivo específico:

`docker load --input {{caminho/para/arquivo_imagem.tar}}`

- Carregar uma imagem do Docker a partir de um arquivo específico no modo silencioso:

`docker load --quiet --input {{caminho/para/arquivo_imagem.tar}}`
