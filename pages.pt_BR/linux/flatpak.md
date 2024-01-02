# flatpak

> Construa, instale e execute aplicações e plataformas flatpak.
> Mais informações: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Executa uma aplicação instalada:

`flatpak run {{nome}}`

- Instala uma aplicação de uma fonte remota:

`flatpak install {{remoto}} {{nome}}`

- Lista todas as aplicações e plataformas instaladas:

`flatpak list`

- Atualiza todas as aplicações e plataformas instaladas:

`flatpak update`

- Adiciona uma fonte remota:

`flatpak remote-add --if-not-exists {{nome_remoto}} {{url_remoto}}`

- Lista todas fontes remotas configuradas:

`flatpak remote-list`

- Remove uma aplicação instalada:

`flatpak remove {{nome}}`

- Mostra informações sobre uma aplicação instalada:

`flatpak info {{nome}}`
