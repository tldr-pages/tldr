# doctl apps

> A digitalocean alkalmazások kezelésére szolgál. További információ: <https://docs.digitalocean.com/reference/doctl/reference/apps>.

- Alkalmazás létrehozása:

`doctl apps create`

- Telepítés létrehozása egy adott alkalmazáshoz:

`doctl apps create-deployment {{app_id}}`

- Alkalmazás törlése interaktívan:

`doctl apps delete {{app_id}}`

- Egy alkalmazás lekérdezése:

`doctl apps get`

- Az összes alkalmazás listázása:

`doctl apps list`

- Egy adott alkalmazás összes telepítésének listázása:

`doctl apps list-deployments {{app_id}}`

- Naplók lekérése egy adott alkalmazásból:

`doctl apps logs {{app_id}}`

- Egy adott alkalmazás frissítése egy adott alkalmazás specifikációjával:

`doctl apps update {{app_id}} --spec {{path/to/spec.yml}}`
