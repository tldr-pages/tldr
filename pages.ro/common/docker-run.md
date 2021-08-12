# docker run

> Rulați o comandă într-un container Docker nou.
> Mai multe informaţii: <https://docs.docker.com/engine/reference/commandline/run/>

- Rulați comanda într-un container nou dintr-o imagine etichetată:

`docker run {{image:tag}} {{command}}`

- Rulați comanda într-un container nou în fundal și afișați ID-ul său:

`docker run -d {{image}} {{command}}`

- Rulați comanda într-un container one-off în modul interactiv și pseudo-tty:

`docker run --rm -it {{image}} {{command}}`

- Rulați comanda într-un container nou cu variabile de mediu trecut:

`docker run -e '{{variable}}={{value}}' -e {{variable}} {{image}} {{command}}`

- Executați comanda într-un container nou cu volume montate legate:

`docker run -v {{path/to/host_path}}:{{path/to/container_path}} {{image}} {{command}}`

- Rulați comanda într-un container nou cu porturi publicate:

`docker run -p {{host_port}}:{{container_port}} {{image}} {{command}}`
