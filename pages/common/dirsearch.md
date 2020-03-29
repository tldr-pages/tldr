# dirsearch

> Web path scanner.
> More information: <https://github.com/maurosoria/dirsearch>.

- Scan a Web server for common paths with common extensions:

`dirsearch --url {{url}} --extensions-list`

- Scan a list of Web servers for common paths with the `.php` extension:

`dirsearch --url-list {{path/to/url-list.txt}} --extensions {{php}}`

- Scan a Web server for user-defined paths with common extensions:

`dirsearch --url {{url}} --extensions-list --wordlist {{path/to/url-paths.txt}}`

- Scan a Web server using a cookie:

`dirsearch --url {{url}} --extensions {{php}} --cookie {{cookie}}`

- Scan a Web server using the `HEAD` HTTP method:

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- Scan a Web server, saving the results to a `.json` file:

`dirsearch --url {{url}} --extensions {{php}} --json-report {{path/to/report.json}}`
