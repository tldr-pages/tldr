# docker service

> A szolgáltatások kezelése egy dokkoló démonon. További információ: <https://docs.docker.com/engine/reference/commandline/service/>.

- A dokkoló démon szolgáltatásainak listázása:

`docker service ls`

- Új szolgáltatás létrehozása:

`docker service create --name {{service_name}} {{image}}:{{tag}}`

- Szolgáltatások szóközzel elválasztott listájának részletes információinak megjelenítése:

`docker service inspect {{service_name|ID}}`

- Szolgáltatások szóközzel elválasztott listájának feladatainak listázása:

`docker service ps {{service_name|ID}}`

- A replikák meghatározott számú replikára való skálázás egy térben elválasztott szolgáltatáslista esetében:

`docker service scale {{service_name}}={{count_of_replicas}}`

- Szolgáltatások szóközzel elválasztott listájának eltávolítása:

`docker service rm {{service_name|ID}}`
