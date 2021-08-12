# cloudflared

> Instrument linie de comandă pentru a crea o conexiune persistentă la rețeaua Cloudflare.
> Mai multe informaţii: <https://developers.cloudflare.com/argo-tunnel/>

- Autentificați și asociați conexiunea la un domeniu din contul Cloudflare:

`cloudflared tunnel login`

- Stabilirea unui tunel către o gazdă în Cloudflare de la serverul local:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}}`

- Stabiliți un tunel către o gazdă în Cloudflare de pe serverul local, fără a verifica certificatul serverului local:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}} --no-tls-verify`

- Salvați jurnalele într-un fișier:

`cloudflared tunnel --hostname {{hostname}} http://localhost:{{port_number}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}}`

- Instalați cloudflared ca serviciu de sistem:

`cloudflared service install`
