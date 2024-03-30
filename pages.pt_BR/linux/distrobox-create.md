# distrobox-create

> Criar um contêiner Distrobox. Veja também: `tldr distrobox`.
> O contêiner criado será integrado ao sistema host, permitindo o compartilhamento do diretório HOME do usuário, armazenamento externo, dispositivos USB externos, aplicativos gráficos (X11/Wayland) e áudio.
> Mais informações: <https://distrobox.it/usage/distrobox-create>.

- Cria um contêiner Distrobox usando a imagem do Ubuntu:

`distrobox-create {{nome_do_contêiner}} --image {{ubuntu:latest}}`

- Clona um contêiner Distrobox:

`distrobox-create --clone {{nome_do_contêiner}} {{nome_do_contêiner_clonado}}`
