# docker service

> Verwalte Docker Services.
> Weitere Informationen: <https://docs.docker.com/engine/reference/commandline/service/>.

- Liste alle Services auf:

`docker service ls`

- Erstelle einen neuen Service:

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- Zeige detaillierte Informationen der mit Leerzeichen separierten Services an:

`docker service inspect {{service_name|ID}}`

- Liste die Tasks der mit Leerzeichen separierten Services auf:

`docker service ps {{service_name|ID}}`

- Skaliere die angegebenen Services auf einen bestimmte Anzahl an Replikaten:

`docker service scale {{service_name}}={{anzahl_an_replikaten}}`

- Lösche die mit Leerzeichen separierten Services:

`docker service rm {{service_name|ID}}`
