# prettier

> Un formator de cod avizat pentru JavaScript, JSON, CSS, YAML și multe altele.
> Mai multe informaţii: <https://prettier.io/>

- Formatați un fișier și imprimați rezultatul la stdout:

`prettier {{path/to/file}}`

- Verificați dacă un anumit fișier a fost formatat:

`prettier --check {{path/to/file}}`

- Rulați cu un fișier de configurare specific:

`prettier --config {{path/to/config_file}} {{path/to/file}}`

- Formatați un fișier sau un director, înlocuind originalul:

`prettier --write {{path/to/file_or_directory}}`

- Formatarea fișierelor sau directoarelor recursiv folosind ghilimele unice și fără virgule:

`prettier --single-quote --trailing-comma {{none}} --write {{path/to/file_or_directory}}`
