# run0

> Eleva privilégios interativamente.
> Similar ao `sudo`, mas não é um binário SUID, a autenticação acontece via polkit, e comandos são executados a partir de um serviço do `systemd`.
> Veja também: `sudo`, `pkexec`, `doas`.
> Mais informações: <https://www.freedesktop.org/software/systemd/man/latest/run0.html>.

- Executa um comando como root:

`run0 {{comando}}`

- Executa um comando como outro usuário e/ou grupo:

`run0 {{[-u|--user]}} {{usuário|uid}} {{[-g|--group]}} {{nome_do_grupo|gid}} {{comando}}`
