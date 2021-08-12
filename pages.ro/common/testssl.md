# testssl

> Verificați protocoalele și cifrurile SSL/TLS acceptate de un server.
> Mai multe informaţii: <https://testssl.sh/>

- Testați un server (executați fiecare verificare) pe portul 443:

`testssl {{example.com}}`

- Testați un alt port:

`testssl {{example.com:465}}`

- Verifică doar protocoalele disponibile:

`testssl --protocols {{example.com}}`

- Verifică doar vulnerabilităţile:

`testssl --vulnerable {{example.com}}`

- Verificați numai anteturile de securitate HTTP:

`testssl --headers {{example.com}}`
