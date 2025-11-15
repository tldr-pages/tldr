# pidof

> Ottiene l'ID di un processo a partire dal suo nome.
> Maggiori informazioni: <https://manned.org/pidof>.

- Elenca gli ID di tutti i processi con un dato nome:

`pidof {{bash}}`

- Elenca un solo ID di processo con il nome specificato:

`pidof -s {{bash}}`

- Elenca gli ID dei processi con un dato includendo anche gli script:

`pidof -x {{script.py}}`

- Uccide tutti i processi con un dato nome:

`kill $(pidof {{nome}})`
