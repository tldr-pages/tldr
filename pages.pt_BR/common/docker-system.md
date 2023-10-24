# docker system

> Gerenciar dados do Docker e exibir informações do sistema em todo o sistema.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/system/>.

- Mostrar ajuda:

`docker system`

- Mostrar o uso de disco do Docker:

`docker system df`

- Mostrar informações detalhadas sobre o uso de disco:

`docker system df --verbose`

- Remover dados não utilizados:

`docker system prune`

- Remover dados não utilizados criados há mais de um período específico no passado:

`docker system prune --filter="until={{horas}}h{{minutos}}m"`

- Exibir eventos em tempo real do daemon do Docker:

`docker system events`

- Exibir eventos em tempo real de contêineres transmitidos como JSON Lines válidos:

`docker system events --filter 'type=container' --format '{{json .}}'`

- Exibir informações em todo o sistema:

`docker system info`
