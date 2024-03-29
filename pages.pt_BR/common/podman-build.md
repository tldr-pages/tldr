# podman build

> Ferramenta sem daemon para criar imagens de contêiner.
> O Podman fornece uma linha de comando comparável ao Docker-CLI. Simplificando: `alias docker=podman`.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-build.1.html>.

- Cria uma imagem usando um `Dockerfile` ou `Containerfile` no diretório especificado:

`podman build {{caminho/para/diretório}}`

- Cria uma imagem com uma tag especificada:

`podman build --tag {{nome_da_imagem:versão}} {{caminho/para/diretório}}`

- Cria uma imagem a partir de um arquivo não padrão:

`podman build --file {{Containerfile.diferente}} .`

- Cria uma imagem sem usar nenhuma imagem em cache previamente:

`podman build --no-cache {{caminho/para/diretório}}`

- Cria uma imagem suprimindo todas as saídas:

`podman build --quiet {{caminho/para/diretório}}`
