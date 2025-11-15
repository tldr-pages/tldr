# flatpak

> Constrói, instala e executa aplicações e plataformas flatpak.
> Mais informações: <https://docs.flatpak.org/en/latest/flatpak-command-reference.html#flatpak>.

- Executa uma aplicação instalada:

`flatpak run {{com.exemplo.aplicacao}}`

- Instala uma aplicação de uma fonte remota:

`flatpak install {{nome_remoto}} {{com.exemplo.aplicacao}}`

- Lista aplicações instaladas, ignorando plataformas:

`flatpak list --app`

- Atualiza todas as aplicações e plataformas instaladas:

`flatpak update`

- Adiciona uma fonte remota:

`flatpak remote-add --if-not-exists {{nome_remoto}} {{url_remoto}}`

- Remove uma aplicação instalada:

`flatpak remove {{com.exemplo.aplicacao}}`

- Remove todos as aplicações não usadas:

`flatpak remove --unused`

- Mostra informações sobre uma aplicação instalada:

`flatpak info {{com.exemplo.aplicacao}}`
