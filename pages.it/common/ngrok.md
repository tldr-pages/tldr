# ngrok

> Reverse proxy che crea un tunnel sicuro da un endpoint pubblico a un servizio web in esecuzione in locale.
> Maggiori informazioni: <https://ngrok.com/docs/agent/cli>.

- Esponi un servizio HTTP locale su una determinata porta:

`ngrok http {{80}}`

- Esponi un servizio HTTP locale su un host specifico:

`ngrok http {{example.com}}:{{80}}`

- Esponi un server HTTPS locale:

`ngrok http https://localhost`

- Esponi il traffico TCP su una determinata porta:

`ngrok tcp {{22}}`

- Esponi il traffico TLS per un host e una porta specifici:

`ngrok tls -hostname={{example.com}} {{443}}`
