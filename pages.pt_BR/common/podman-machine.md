# podman machine

> Criar e gerenciar máquinas virtuais executando o Podman.
> Incluído com a versão 4 ou superior do Podman.
> Mais informações: <https://docs.podman.io/en/latest/markdown/podman-machine.1.html>.

- Listar as máquinas existentes:

`podman machine ls`

- Criar uma nova máquina padrão:

`podman machine init`

- Criar uma nova máquina com um nome específico:

`podman machine init {{nome}}`

- Criar uma nova máquina com recursos diferentes:

`podman machine init --cpus={{4}} --memory={{4096}} --disk-size={{50}}`

- Iniciar ou parar uma máquina:

`podman machine {{start|stop}} {{nome}}`

- Conectar-se a uma máquina em execução via SSH:

`podman machine ssh {{nome}}`

- Inspecionar informações sobre uma máquina:

`podman machine inspect {{nome}}`
