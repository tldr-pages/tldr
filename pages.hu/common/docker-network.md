# docker network

> Docker hálózatok létrehozása és kezelése. További információ: <https://docs.docker.com/engine/reference/commandline/network/>.

- Az összes elérhető és konfigurált hálózat listázása a docker démonon:

`docker network ls`

- Felhasználó által definiált hálózat létrehozása:

`docker network create --driver {{driver_name}} {{network_name}}`

- Hálózatok szóközzel elválasztott listájának részletes információinak megjelenítése:

`docker network inspect {{network_name}}`

- Egy konténer csatlakoztatása egy hálózathoz egy név vagy azonosító segítségével:

`docker network connect {{network_name}} {{container_name|ID}}`

- Konténer leválasztása egy hálózatról:

`docker network disconnect {{network_name}} {{container_name|ID}}`

- Az összes nem használt (egyetlen konténer által sem hivatkozott) hálózat eltávolítása:

`docker network prune`

- A nem használt hálózatok szóközzel elválasztott listájának eltávolítása:

`docker network rm {{network_name}}`
