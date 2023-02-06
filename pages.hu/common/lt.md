# lt

> A localtunnel a világ számára is elérhetővé teszi a localhostot a könnyű tesztelés és megosztás érdekében. További információ: <https://github.com/localtunnel/localtunnel>.

- Alagút indítása egy adott portról:

`lt --port {{8000}}`

- Adja meg a továbbítást végző upstream kiszolgálót:

`lt --port {{8000}} --host {{host}}`

- Kérjen egy adott aldomain-t:

`lt --port {{8000}} --subdomain {{subdomain}}`

- Alapvető kérési információk nyomtatása:

`lt --port {{8000}} --print-requests`

- Az alagút URL-címének megnyitása az alapértelmezett webböngészőben:

`lt --port {{8000}} --open`
