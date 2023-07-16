# docker inspect

> Retorna informações de baixo nível sobre objetos do Docker.
> Mais informações: <https://docs.docker.com/engine/reference/commandline/inspect/>.

- Exibir ajuda:

`docker inspect`

- Exibir informações sobre um contêiner, imagem ou volume usando um nome ou ID:

`docker inspect {{contêiner|imagem|ID}}`

- Exibir o endereço IP de um contêiner:

`docker inspect --format='{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' {{contêiner}}`

- Exibir o caminho para o arquivo de log do contêiner:

`docker inspect --format='{{.LogPath}}' {{contêiner}}`

- Exibir o nome da imagem do contêiner:

`docker inspect --format='{{.Config.Image}}' {{contêiner}}`

- Exibir as informações de configuração como JSON:

`docker inspect --format='{{json .Config}}' {{contêiner}}`

- Exibir todas as portas vinculadas:

`docker inspect --format='{{range $p, $conf := .NetworkSettings.Ports}} {{$p}} -> {{(index $conf 0).HostPort}} {{end}}' {{contêiner}}`
