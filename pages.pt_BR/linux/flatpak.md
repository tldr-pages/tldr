# flatpak

> Construa, instale e execute aplicações flatpak e plataformas.
> Mais informações: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Executar uma aplicação instalada:

`flatpak run {{name}}`

- Instalar uma aplicação de uma fonte remota:

`flatpak install {{remote}} {{name}}`

- Listar todas as aplicações e plataformas instaladas:

`flatpak list`

- Atualizar todas as aplicações e plataformas instaladas:

`flatpak update`

- Adicionar uma fonte remota:

`flatpak remote-add --if-not-exists {{remote_name}} {{remote_url}}`

- Listar todas fontes remotas configuradas:

`flatpak remote-list`

- Remover uma aplicação instalada:

`flatpak remove {{name}}`

- Mostrar informações sobre uma aplicação instalada:

`flatpak info {{name}}`
