# podman machine

> Criar e gerenciar máquinas virtuais executando o Podman.
> Incluído com a versão 4 ou superior do Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Lista as máquinas existentes:

`podman machine ls`

- Cria uma nova máquina padrão:

`podman machine init`

- Cria uma nova máquina com um nome específico:

`podman machine init {{nome}}`

- Cria uma nova máquina com recursos diferentes:

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- Inicia ou para uma máquina:

`podman machine {{start|stop}} {{nome}}`

- Conecta-se a uma máquina em execução via SSH:

`podman machine ssh {{nome}}`

- Inspeciona informações sobre uma máquina:

`podman machine inspect {{nome}}`
