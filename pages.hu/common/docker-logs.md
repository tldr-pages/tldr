# docker logs

> Konténernaplók nyomtatása. További információ: <https://docs.docker.com/engine/reference/commandline/logs>.

- Naplók nyomtatása konténerből:

`docker logs {{container_name}}`

- Naplók nyomtatása és követése:

`docker logs -f {{container_name}}`

- Utolsó 5 sor nyomtatása:

`docker logs {{container_name}} --tail {{5}}`

- Naplók nyomtatása és időbélyegekkel való kiegészítése:

`docker logs -t {{container_name}}`

- Naplók nyomtatása a konténer végrehajtásának egy bizonyos időpontjától (pl. 23m, 10s, 2013-01-02T13:23:37):

`docker logs {{container_name}} --until {{time}}`
