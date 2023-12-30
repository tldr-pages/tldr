# docker system

> Gerenciar dados do Docker e exibir informações do sistema em todo o sistema.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/system/>.

- Mostra ajuda:

`docker system`

- Mostra o uso de disco do Docker:

`docker system df`

- Mostra informações detalhadas sobre o uso de disco:

`docker system df --verbose`

- Remove dados não utilizados:

`docker system prune`

- Remove dados não utilizados criados há mais de um período específico no passado:

`docker system prune --filter "until={{horas}}h{{minutos}}m"`

- Exibe eventos em tempo real do daemon do Docker:

`docker system events`

- Exibe eventos em tempo real de contêineres transmitidos como JSON Lines válidos:

`docker system events --filter 'type=container' --format '{{json .}}'`

- Exibe informações em todo o sistema:

`docker system info`
