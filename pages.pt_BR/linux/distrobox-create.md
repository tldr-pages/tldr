# distrobox-create

> Criar um contêiner distrobox. Veja também: `tldr distrobox`.
> O contêiner criado será integrado ao sistema host, permitindo o compartilhamento do diretório HOME do usuário, armazenamento externo, dispositivos USB externos, aplicativos gráficos (X11/Wayland) e áudio.
> Mais informações: <https://distrobox.privatedns.org/usage/distrobox-create.html>.

- Criar um contêiner distrobox usando a imagem do Ubuntu:

`distrobox-create {{nome_do_contêiner}} --image {{ubuntu:latest}}`

- Clonar um contêiner distrobox:

`distrobox-create --clone {{nome_do_contêiner}} {{nome_do_contêiner_clonado}}`
