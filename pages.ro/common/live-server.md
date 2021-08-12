# live-server

> Un server http simplu de dezvoltare cu capacitate de reîncărcare în direct.
> Mai multe informaţii: <https://www.npmjs.com/package/live-server>

- Serviți un fișier `index.html` și reîncărcați modificările:

`live-server`

- Specificați un port (implicit este 8080) din care să servească un fișier:

`live-server --port={{8081}}`

- Specificați un fișier dat pentru a servi:

`live-server --open={{about.html}}`

- Proxy toate cererile pentru ROUTE la URL:

`live-server --proxy={{/}}:{{http:localhost:3000}}`
