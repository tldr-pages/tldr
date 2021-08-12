# docker logs

> Imprimare jurnalele containerelor.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/logs>

- Imprimarea jurnalelor dintr-un container:

`docker logs {{container_name}}`

- Imprimați jurnalele și urmați-le:

`docker logs -f {{container_name}}`

- Print ultimele 5 linii:

`docker logs {{container_name}} --tail {{5}}`

- Imprimați jurnalele și adăugați-le cu marcaje temporale:

`docker logs -t {{container_name}}`

- Imprimarea jurnalelor dintr-un anumit punct în timp de execuție a containerului (adică 23m, 10s, 2013-01-02T 13:23:37):

`docker logs {{container_name}} --until {{time}}`
