# docker compose

> Több konténeres dokkoló alkalmazások futtatása és kezelése. További információ: <https://docs.docker.com/compose/reference/>.

- Az összes futó konténer listázása:

`docker compose ps`

- Az összes konténer létrehozása és indítása a háttérben az aktuális könyvtárból egy `docker-compose.yml` fájl segítségével:

`docker compose up -d`

- Indítsa el az összes konténert, szükség esetén építse újra:

`docker compose up --build`

- Indítsa el az összes konténert egy alternatív kompozíciós fájl segítségével:

`docker compose --file {{path/to/file}} up`

- Az összes futó konténer leállítása:

`docker compose stop`

- Az összes konténer, hálózat, kép és kötet leállítása és eltávolítása:

`docker compose down --rmi all --volumes`

- Kövesse az összes konténer naplóit:

`docker compose logs --follow`

- Egy adott konténer naplóinak követése:

`docker compose logs --follow {{container_name}}`
