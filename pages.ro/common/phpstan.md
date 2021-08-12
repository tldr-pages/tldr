# phpstan

> Un instrument de analiză statică PHP pentru a descoperi bug-uri în cod.
> Mai multe informaţii: <https://github.com/phpstan/phpstan>

- Afișează opțiunile disponibile pentru analiză:

`phpstan analyse --help`

- Analizaţi directoarele separate de spaţiu specificate:

`phpstan analyse {{path/to/directory}}`

- Analizați un director utilizând un fișier de configurare:

`phpstan analyse {{path/to/directory}} --configuration {{path/to/config}}`

- Analiza folosind un nivel specific de regulă (0-7, mai mare este mai strictă):

`phpstan analyse {{path/to/directory}} --level {{level}}`

- Specificați un fișier autoload pentru a încărca înainte de a analiza:

`phpstan analyse {{path/to/directory}} --autoload-file {{path/to/autoload_file}}`

- Specificați o limită de memorie în timpul analizei:

`phpstan analyse {{path/to/directory}} --memory-limit {{memory_limit}}`
