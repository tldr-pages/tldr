# dockerd

> Um processo persistente para iniciar e gerenciar contêineres Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/dockerd/>.

- Executar o daemon do Docker:

`dockerd`

- Executar o daemon do Docker e configurá-lo para escutar em sockets específicos (UNIX e TCP):

`dockerd --host unix://{{caminho/para/tmp.sock}} --host tcp://{{ip}}`

- Executar com um arquivo PID específico para o daemon:

`dockerd --pidfile {{caminho/para/arquivo_pid}}`

- Executar no modo de depuração:

`dockerd --debug`

- Executar e definir um nível de log específico:

`dockerd --log-level={{debug|info|warn|error|fatal}}`
