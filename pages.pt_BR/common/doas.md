# doas

> Executa um comando como outro usuário.
> Veja também: `sudo`, `pkexec`, `run0`.
> Mais informações: <https://man.openbsd.org/doas>.

- Executa um comando como root:

`doas {{comando}}`

- Executa um comando como outro usuário:

`doas -u {{usuario}} {{comando}}`

- Executa o shell padrão como root:

`doas -s`

- Lê um arquivo de configuração e verifica se a execução de um comando como outro usuário é permitida:

`doas -C {{caminho/para/arquivo_de_configuração}} {{comando}}`

- Faz com que o `doas` solicite uma senha mesmo que já tenha sido inserida anteriormente:

`doas -L`
