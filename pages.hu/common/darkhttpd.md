# darkhttpd

> Darkhttpd webszerver. További információ: <https://unix4lyfe.org/darkhttpd>.

- A megadott dokumentumgyökeret kiszolgáló szerver elindítása:

`darkhttpd {{path/to/docroot}}`

- A szerver elindítása a megadott porton (alapértelmezés szerint a 8080-as porton, ha nem root felhasználóként fut):

`darkhttpd {{path/to/docroot}} --port {{port}}`

- Csak a megadott IP-címen figyeljen (alapértelmezés szerint a szerver minden interfészen figyel):

`darkhttpd {{path/to/docroot}} --addr {{ip_address}}`
