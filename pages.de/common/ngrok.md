# ngrok

> Reverse-Proxy, welcher einen sicheren Tunnel von einem öffentlichen Endpunkt zu einem lokal verfügbaren Webservice erstellt.
> Weitere Informationen: <https://ngrok.com>.

- Veröffentliche einen lokalen HTTP-Service auf dem angegebenen Port:

`ngrok http {{80}}`

- Veröffentliche einen lokalen HTTP-Service auf einem bestimmten Host:

`ngrok http {{beispiel.dev}}:{{80}}`

- Veröffentliche einen lokalen HTTPS-Server:

`ngrok http https://localhost`

- Veröffentliche den TCP-Traffic auf dem angegebenen Port:

`ngrok tcp {{22}}`

- Veröffentliche den TLS-Traffic für einen bestimmten Host und Port:

`ngrok tls -hostname={{beispiel.de}} {{443}}`
