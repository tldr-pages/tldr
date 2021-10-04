# flatpak

> Construa, instale e execute aplicações e plataformas flatpak.
> Mais informações: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Executar uma aplicação instalada:

`flatpak run {{nome}}`

- Instalar uma aplicação de uma fonte remota:

`flatpak install {{remoto}} {{nome}}`

- Listar todas as aplicações e plataformas instaladas:

`flatpak list`

- Atualizar todas as aplicações e plataformas instaladas:

`flatpak update`

- Adicionar uma fonte remota:

`flatpak remote-add --if-not-exists {{nome_remoto}} {{url_remoto}}`

- Listar todas fontes remotas configuradas:

`flatpak remote-list`

- Remover uma aplicação instalada:

`flatpak remove {{nome}}`

- Mostrar informações sobre uma aplicação instalada:

`flatpak info {{nome}}`
