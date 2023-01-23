# cloudflared

> Parancssori eszköz a Cloudflare hálózathoz való tartós kapcsolat létrehozásához. További információ: <https://developers.cloudflare.com/argo-tunnel/>.

- Hitelesítse és társítsa a kapcsolatot egy tartományhoz a Cloudflare-fiókban:

`cloudflared tunnel login`

- Alagút létrehozása a helyi kiszolgálóról a Cloudflare egyik állomásához:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}}`

- Alagút létrehozása a helyi kiszolgálóról a Cloudflare egy állomásához a helyi kiszolgáló tanúsítványának ellenőrzése nélkül:

`cloudflared tunnel --hostname {{hostname}} localhost:{{port_number}} --no-tls-verify`

- Naplók mentése egy fájlba:

`cloudflared tunnel --hostname {{hostname}} http://localhost:{{port_number}} --loglevel {{panic|fatal|error|warn|info|debug}} --logfile {{path/to/file}}`

- A Cloudflared telepítése rendszerszolgáltatásként:

`cloudflared service install`
