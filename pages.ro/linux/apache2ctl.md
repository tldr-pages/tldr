# apache2ctl

> Instrumentul CLI pentru administrarea serverului web HTTP Apache.
> Această comandă vine cu OS-uri bazate pe Debian, pentru cele bazate pe RHEL vezi `httpd`.
> Mai multe informaţii: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>

- Porneşte demonul apaşilor. Aruncați un mesaj dacă acesta este deja în execuție:

`sudo apache2ctl start`

- Opreşte demonul apaşilor.

`sudo apache2ctl stop`

- Reporniţi daemonul apaşilor:

`sudo apache2ctl restart`

- Sintaxa de testare a fișierului de configurare:

`sudo apache2ctl -t`

- Lista modulelor încărcate:

`sudo apache2ctl -M`
