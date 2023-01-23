# podman-compose

> Compose Specification konténer definíciójának futtatása és kezelése. További információ: <https://github.com/containers/podman-compose>.

- Az összes futó konténer listázása:

`podman-compose ps`

- Létrehozza és elindítja az összes konténert a háttérben egy helyi `docker-compose.yml` segítségével:

`podman-compose up -d`

- Az összes konténer elindítása, szükség esetén építése:

`podman-compose up --build`

- Indítsa el az összes konténert egy alternatív compose fájl segítségével:

`podman-compose {{path/to/file}} up`

- Az összes futó konténer leállítása:

`podman-compose stop`

- Az összes konténer, hálózat és kötet eltávolítása:

`podman-compose down --volumes`

- Kövesse a konténerek naplóit (hagyja ki az összes konténer nevét):

`podman-compose logs --follow {{container_name}}`

- Egyszeri parancs futtatása egy olyan szolgáltatásban, amelynek nincsenek leképezve portjai:

`podman-compose run {{service_name}} {{command}}`
