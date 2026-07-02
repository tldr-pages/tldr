# cockpit-ws

> Comunica tra l'applicazione browser e vari strumenti di configurazione e servizi come `cockpit-bridge`.
> Maggiori informazioni: <https://cockpit-project.org/guide/latest/cockpit-ws.8.html>.

- Avvia con autenticazione tramite SSH su `127.0.0.1` con porta `22` abilitata:

`cockpit-ws --local-ssh`

- Avvia un server HTTP su una porta specifica:

`cockpit-ws --port {{port}}`

- Avvia e si associa a un indirizzo IP specifico (predefinito `0.0.0.0`):

`cockpit-ws --address {{ip_address}}`

- Avvia senza TLS:

`cockpit-ws --no-tls`

- Mostra aiuto:

`cockpit-ws --help`
