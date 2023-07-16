# docker tag

> Atribuir tags a imagens Docker existentes.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/tag/>.

- Atribuir um nome e tag a um ID de imagem específico:

`docker tag {{id}} {{nome}}:{{tag}}`

- Atribuir uma tag a uma imagem específica:

`docker tag {{imagem}}:{{tag_atual}} {{imagem}}:{{nova_tag}}`

- Exibir ajuda:

`docker tag`
