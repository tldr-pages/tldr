# tailscale

> Egy privát WireGuard hálózati szolgáltatás. Egyes alparancsok, mint például a `tailscale up`, saját használati dokumentációval rendelkeznek. További információ: <https://tailscale.com>.

- Csatlakozás a Tailscale-hoz:

`sudo tailscale up`

- Kapcsolat megszakítása a Tailscale-hez:

`sudo tailscale down`

- Az aktuális Tailscale IP-címek megjelenítése:

`tailscale ip`

- Pingeljen egy Tailscale-rétegben lévő társas csomópontot, és mutassa meg, hogy az egyes válaszok melyik útvonalon érkeztek:

`tailscale ping {{ip|hostname}}`

- A helyi hálózati feltételek elemzése és az eredmény megjelenítése:

`tailscale netcheck`

- A Tailscale vezérlésére szolgáló webkiszolgáló elindítása:

`tailscale web`

- Megosztható azonosító megjelenítése a problémák diagnosztizálásához:

`tailscale bugreport`

- Segítség megjelenítése egy alparancshoz:

`tailscale {{subcommand}} --help`
