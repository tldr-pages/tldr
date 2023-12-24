# dash

> Debian Almquist Shell, uma implementação moderna e compatível com POSIX de `sh` (não compatível com Bash).
> Mais informações: <https://manned.org/dash>.

- Inicia uma sessão de shell interativa:

`dash`

- Executa [c]omandos específicos:

`dash -c "{{echo 'dash executado'}}"`

- Executa um script específico:

`dash {{caminho/para/script.sh}}`

- Checar erros de sintaxe em um script específico:

`dash -n {{caminho/para/script.sh}}`

- Executa comandos de um script, imprimindo cada comando antes de executá-lo:

`dash -x {{caminho/para/script.sh}}`

- Executa comandos de um script, parando no primeiro [e]rro:

`dash -e {{caminho/para/script.sh}}`

- Executa comandos específicos de `stdin`:

`{{echo "echo 'dash executado'"}} | dash`
