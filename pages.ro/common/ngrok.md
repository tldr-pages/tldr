# ngrok

> Proxy inversă care creează un tunel securizat de la un punct final public la un serviciu web care rulează local.
> Mai multe informaţii: <https://ngrok.com>

- Expuneți un serviciu HTTP local pe un anumit port:

`ngrok http {{80}}`

- Expuneți un serviciu HTTP local pe o anumită gazdă:

`ngrok http {{foo.dev}}:{{80}}`

- Expune un server HTTPS local:

`ngrok http https://localhost`

- Expune traficul TCP pe un anumit port:

`ngrok tcp {{22}}`

- Expune traficul TLS pentru o anumită gazdă și port:

`ngrok tls -hostname={{foo.com}} {{443}}`
