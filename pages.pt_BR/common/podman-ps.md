# podman ps

> Listar contêineres do Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-ps.1.html>.

- Lista contêineres do Podman em execução atualmente:

`podman ps`

- Lista todos os contêineres do Podman (em execução e parados):

`podman ps {{[-a|--all]}}`

- Mostra o contêiner mais recente criado (inclui todos os estados):

`podman ps {{[-l|--latest]}}`

- Filtra contêineres que contêm uma substring em seus nomes:

`podman ps {{[-f|--filter]}} "name={{nome}}"`

- Filtra contêineres que compartilham uma determinada imagem como ancestral:

`podman ps {{[-f|--filter]}} "ancestor={{imagem}}:{{tag}}"`

- Filtra contêineres pelo código de status de saída:

`podman ps {{[-af|--all --filter]}} "exited={{código}}"`

- Filtra contêineres pelo status (criado, em execução, removendo, pausado, encerrado e morto):

`podman ps {{[-f|--filter]}} "status={{status}}"`

- Filtra contêineres que montam um volume específico ou têm um volume montado em um caminho específico:

`podman ps {{[-f|--filter]}} "volume={{caminho/para/diretório}}" --format "table {{.ID}}\t{{.Image}}\t{{.Names}}\t{{.Mounts}}"`
