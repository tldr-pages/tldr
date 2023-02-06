# ngrok

> Fordított proxy, amely biztonságos alagutat hoz létre egy nyilvános végpontról egy helyben futó webszolgáltatáshoz. További információ: <https://ngrok.com>.

- Helyi HTTP-szolgáltatás feltárása egy adott porton:

`ngrok http {{80}}`

- Helyi HTTP-szolgáltatás feltárása egy adott állomáson:

`ngrok http {{foo.dev}}:{{80}}`

- Helyi HTTPS-kiszolgáló feltárása:

`ngrok http https://localhost`

- TCP-forgalom feltárása egy adott porton:

`ngrok tcp {{22}}`

- TLS-forgalom feltárása egy adott állomáson és porton:

`ngrok tls -hostname={{foo.com}} {{443}}`
