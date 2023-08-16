# podman ps

> Listar contêineres do Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Listar contêineres do Podman em execução atualmente:

`podman ps`

- Listar todos os contêineres do Podman (em execução e parados):

`podman ps --all`

- Mostrar o contêiner mais recente criado (inclui todos os estados):

`podman ps --latest`

- Filtrar contêineres que contenham uma substring em seus nomes:

`podman ps --filter "name={{nome}}"`

- Filtrar contêineres que compartilhem uma determinada imagem como ancestral:

`podman ps --filter "ancestor={{imagem}}:{{tag}}"`

- Filtrar contêineres pelo código de status de saída:

`podman ps --all --filter "exited={{código}}"`

- Filtrar contêineres pelo status (criado, em execução, removendo, pausado, encerrado e morto):

`podman ps --filter "status={{status}}"`

- Filtrar contêineres que montam um volume específico ou têm um volume montado em um caminho específico:

`podman ps --filter "volume={{caminho/para/diretório}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
