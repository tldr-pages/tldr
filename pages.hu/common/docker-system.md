# docker system

> A Docker-adatok kezelése és a rendszerre vonatkozó információk megjelenítése. További információ: <https://docs.docker.com/engine/reference/commandline/system/>.

- Súgó megjelenítése:

`docker system`

- Docker lemezhasználat megjelenítése:

`docker system df`

- Részletes információk megjelenítése a lemezhasználatról:

`docker system df --verbose`

- A nem használt adatok eltávolítása:

`docker system prune`

- A megadott időn túl létrehozott, nem használt adatok eltávolítása:

`docker system prune --filter="until={{hours}}h{{minutes}}m"`

- A Docker démon valós idejű eseményeinek megjelenítése:

`docker system events`

- Érvényes JSON sorokként streamelt konténerek valós idejű eseményeinek megjelenítése:

`docker system events --filter 'type=container' --format '{{json .}}'`

- Rendszer szintű információk megjelenítése:

`docker system info`
