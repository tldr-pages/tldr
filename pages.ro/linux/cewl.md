# cewl

> URL spidering instrument pentru a face o listă de cuvinte cracare din conținutul web.
> Mai multe informaţii: <https://digi.ninja/projects/cewl.php>

- Creați un fișier listă de cuvinte de la adresa URL dată până la 2 adâncime de linkuri:

`cewl --depth {{2}} --write {{path/to/wordlist.txt}} {{url}}`

- Ieșiți o listă de cuvinte alfanumerice din URL-ul dat cu cuvinte de minim 5 caractere:

`cewl --with-numbers --min_word_length {{5}} {{url}}`

- Ieșiți o listă de cuvinte din adresa URL dată în modul de depanare, inclusiv adresele de e-mail:

`cewl --debug --email {{url}}`

- Ieșiți o listă de cuvinte din adresa URL dată utilizând autentificarea HTTP Basic sau Digest:

`cewl --auth_type {{basic|digest}} --auth_user {{username}} --auth_pass {{password}} {{url}}`

- Ieșiți o listă de cuvinte din adresa URL dată printr-un proxy:

`cewl --proxy_host {{host}} --proxy_port {{port}} {{url}}`
