# flyctl

> A flyctl.io parancssori eszköze. További információ: <https://github.com/superfly/flyctl>.

- Jelentkezzen be egy Fly-fiókba:

`flyctl auth login`

- Alkalmazás indítása egy adott Dockerfájlból (az alapértelmezett elérési út az aktuális munkakönyvtár):

`flyctl launch --dockerfile {{path/to/dockerfile}}`

- Az aktuálisan telepített alkalmazás megnyitása az alapértelmezett webböngészőben:

`flyctl open`

- A Fly alkalmazások telepítése egy adott Dockerfile-ból:

`flyctl deploy --dockerfile {{path/to/dockerfile}}`

- Az aktuális alkalmazás Fly Web UI-jának megnyitása egy webböngészőben:

`flyctl dashboard`

- A bejelentkezett Fly-fiókban lévő összes alkalmazás listázása:

`flyctl apps list`

- Egy adott futó alkalmazás állapotának megtekintése:

`flyctl status --app {{app_name}}`

- Verzióinformációk megjelenítése:

`flyctl version`
