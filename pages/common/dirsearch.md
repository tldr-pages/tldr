# dirsearch

> Web path scanner.
> More information: <https://github.com/maurosoria/dirsearch>.

- Scan a web server for common paths with common extensions:

`dirsearch {{[-u|--url]}} {{url}} --extensions-list`

- Scan a list of web servers for common paths with given file extensions:

`dirsearch {{[-l|--url-list]}} {{path/to/url-list.txt}} {{[-e|--extensions]}} {{php,jsp,aspx,...}}`

- Scan a web server for user-defined paths with common extensions:

`dirsearch {{[-u|--url]}} {{url}} --extensions-list {{[-w|--wordlists]}} {{path/to/url-paths1.txt,path/to/url-paths2.txt,...}}`

- Scan a web server using a cookie:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} --cookie {{cookie}}`

- Scan a web server using the `HEAD` HTTP method:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} {{[-m|--http-method]}} {{HEAD}}`

- Scan a web server, saving the results to a `.json` file:

`dirsearch {{[-u|--url]}} {{url}} {{[-e|--extensions]}} {{php}} --json-report {{path/to/report.json}}`
