# distrobox-enter

> Entrar em um contêiner distrobox. Veja também: `tldr distrobox`.
> O comando padrão executado é o seu SHELL, mas você pode especificar shells diferentes ou comandos completos para serem executados.
> Se usado dentro de um script, um aplicativo ou um serviço, você pode usar o modo `--headless` para desabilitar o tty e a interatividade.
> Mais informações: <https://distrobox.privatedns.org/usage/distrobox-enter.html>.

- Entrar em um contêiner distrobox:

`distrobox-enter {{nome_do_contêiner}}`

- Entrar em um contêiner distrobox e executar um comando no login:

`distrobox-enter {{nome_do_contêiner}} -- {{sh -l}}`

- Entrar em um contêiner distrobox sem instanciar um tty:

`distrobox-enter --name {{nome_do_contêiner}} -- {{uptime -p}}`
