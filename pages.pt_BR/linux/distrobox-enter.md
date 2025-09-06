# distrobox-enter

> Entrar em um contêiner Distrobox. Veja também: `tldr distrobox`.
> O comando padrão executado é o seu SHELL, mas você pode especificar shells diferentes ou comandos completos para serem executados.
> Se usado dentro de um script, um aplicativo ou um serviço, você pode usar o modo `--headless` para desabilitar o tty e a interatividade.
> Mais informações: <https://distrobox.it/usage/distrobox-enter>.

- Entra em um contêiner Distrobox:

`distrobox-enter {{nome_do_contêiner}}`

- Entra em um contêiner Distrobox e executa um comando no login:

`distrobox-enter {{nome_do_contêiner}} -- {{sh -l}}`

- Entra em um contêiner Distrobox sem instanciar um tty:

`distrobox-enter --name {{nome_do_contêiner}} -- {{uptime -p}}`
