# waitress-serve

> Tiszta Python WSGI HTTP szerver. További információ: <https://docs.pylonsproject.org/projects/waitress/en/latest/runner.html>.

- Egy Python webes alkalmazás futtatása:

`waitress-serve {{import.path:wsgi_func}}`

- Figyeljen a 8080-as porton a localhost-on:

`waitress-serve --listen={{localhost}}:{{8080}} {{import.path:wsgi_func}}`

- Indítsa el a pincérnőt egy Unix socket-en:

`waitress-serve --unix-socket={{path/to/socket}} {{import.path:wsgi_func}}`

- Használjon 4 szálat a kérések feldolgozásához:

`waitress-serve --threads={{4}} {{import.path:wsgifunc}}`

- Hívjon meg egy gyári metódust, amely visszaad egy WSGI objektumot:

`waitress-serve --call {{import.path.wsgi_factory}}`

- Az URL séma beállítása HTTPS-re:

`waitress-serve --url-scheme={{https}} {{import.path:wsgi_func}}`
