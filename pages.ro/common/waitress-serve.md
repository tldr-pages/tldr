# waitress-serve

> Python WSGI Server HTTP.

- Rulați o aplicație web Python:

`waitress-serve {{import.path:wsgi_func}}`

- Ascultă pe portul 8080 pe localhost:

`waitress-serve --listen={{localhost}}:{{8080}} {{import.path:wsgi_func}}`

- Începeți chelnerița pe un soclu Unix:

`waitress-serve --unix-socket={{path/to/socket}} {{import.path:wsgi_func}}`

- Utilizați 4 fire pentru a procesa solicitările:

`waitress-serve --threads={{4}} {{import.path:wsgifunc}}`

- Apelați o metodă din fabrică care returnează un obiect WSGI:

`waitress-serve --call {{import.path.wsgi_factory}}`

- Setați schema URL la https:

`waitress-serve --url-scheme={{https}} {{import.path:wsgi_func}}`
