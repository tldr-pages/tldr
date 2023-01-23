# goaccess

> Nyílt forráskódú, valós idejű webnapló-elemző. További információ: <https://goaccess.io>.

- Egy vagy több naplófájl elemzése interaktív módban:

`goaccess {{path/to/logfile1 path/to/file2 ...}}`

- Használjon egy adott naplóformátumot (vagy előre meghatározott formátumokat, például "kombinált"):

`goaccess {{path/to/logfile}} --log-format={{format}}`

- A `stdin` napló elemzése:

`tail -f {{path/to/logfile}} | goaccess -`

- Elemezzen egy naplót és írja ki egy HTML-fájlba valós időben:

`goaccess {{path/to/logfile}} --output {{path/to/file.html}} --real-time-html`
