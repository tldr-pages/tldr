# dockerd

> Um processo persistente para iniciar e gerenciar contêineres Docker.
> Mais informações: <https://docs.docker.com/reference/cli/dockerd/>.

- Executa o daemon do Docker:

`dockerd`

- Executa o daemon do Docker e configurá-lo para escutar em sockets específicos (UNIX e TCP):

`dockerd {{[-H|--host]}} unix://{{caminho/para/tmp.sock}} {{[-H|--host]}} tcp://{{ip}}`

- Executa com um arquivo PID específico para o daemon:

`dockerd {{[-p|--pidfile]}} {{caminho/para/arquivo_pid}}`

- Executa no modo de depuração:

`dockerd {{[-D|--debug]}}`

- Executa e define um nível de log específico:

`dockerd {{[-l|--log-level]}} {{debug|info|warn|error|fatal}}`
