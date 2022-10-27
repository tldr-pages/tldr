# dash

> Debian Almquist Shell, uma implementação moderna e compatível com POSIX de `sh` (não compatível com Bash).
> Mais informações: <https://manned.org/dash>.

- Inicia uma sessão de shell interativa:

`dash`

- Executa um comando e sai:

`dash -c "{{comando}}"`

- Executa um script:

`dash {{caminho/para/script.sh}}`

- Executa comandos de um script, imprimindo cada comando antes de executá-lo:

`dash -x {{caminho/para/script.sh}}`

- Executa comandos de um script, parando no primeiro erro:

`dash -e {{caminho/para/script.sh}}`

- Lê e executa comandos de stdin:

`dash -s`
