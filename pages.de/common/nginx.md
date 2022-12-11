# nginx

> Nginx Webserver.
> Weitere Informationen: <https://nginx.org/en/>.

- Starte den Server mit der standardmäßigen Konfigurationsdatei:

`nginx`

- Starte den Server mit einer benutzerdefinierten Konfigurationsdatei:

`nginx -c {{konfigurationsdatei}}`

- Starte den Server mit einem Präfix für alle relativen Pfaden in der Konfigurationsdatei:

`nginx -c {{konfigurationsdatei}} -p {{präfix/für/relative/pfade}}`

- Teste die Konfigurationsdatei ohne den laufenden Server zu beeinflussen:

`nginx -t`

- Lade die Konfigurationsdatei durch das Senden eines Signales ohne Pause neu:

`nginx -s reload`
