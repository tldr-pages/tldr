# podman

> Ferramenta de gerenciamento simples para pods, contêineres e imagens.
> O Podman fornece uma linha de comando comparável ao Docker-CLI. Simplificando: `alias docker=podman`.
> Mais informações: <https://github.com/containers/podman/blob/main/commands-demo.md>.

- Lista todos os contêineres (em execução e parados):

`podman ps --all`

- Cria um contêiner a partir de uma imagem, com um nome personalizado:

`podman run --name {{nome_do_contêiner}} {{imagem}}`

- Inicia ou para um contêiner existente:

`podman {{start|stop}} {{nome_do_contêiner}}`

- Baixa uma imagem de um registro (por padrão, Docker Hub):

`podman pull {{imagem}}`

- Exibe a lista de imagens já baixadas:

`podman images`

- Abre um shell dentro de um contêiner que já está em execução:

`podman exec --interactive --tty {{nome_do_contêiner}} {{sh}}`

- Remove um contêiner parado:

`podman rm {{nome_do_contêiner}}`

- Exibe os logs de um ou mais contêineres e acompanha a saída do log:

`podman logs --follow {{nome_do_contêiner}} {{id_do_contêiner}}`
