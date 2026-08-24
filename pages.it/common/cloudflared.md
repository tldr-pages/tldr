# cloudflared

> Crea una connessione persistente alla rete Cloudflare.
> Maggiori informazioni: <https://developers.cloudflare.com/cloudflare-one/networks/connectors/cloudflare-tunnel/>.

- Autentica e associa la connessione a un dominio nell'account Cloudflare:

`cloudflared tunnel login`

- Crea un tunnel con un nome specifico:

`cloudflared tunnel create {{nome}}`

- Stabilisce un tunnel verso un host in Cloudflare dal server locale:

`cloudflared tunnel --hostname {{hostname}} localhost:{{numero_porta}}`

- Stabilisce un tunnel verso un host in Cloudflare dal server locale, senza verificare il certificato del server locale:

`cloudflared tunnel --hostname {{hostname}} localhost:{{numero_porta}} --no-tls-verify`

- Salva i log in un file:

`cloudflared tunnel --hostname {{hostname}} http://localhost:{{numero_porta}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{percorso/del/file}}`

- Installa cloudflared come servizio di sistema:

`cloudflared service install`
