# apache2ctl

> Das CLI Tool um den Apache HTTP Web Server zu administrieren.
> Dieser Command kommt mit Debian basierten Betriebssystemen daher, für RHEL siehe `httpd`.
> Mehr Informationen: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- Starte den Apache daemon. Wirft einen Fehler wenn er bereits läuft:

`sudo apache2ctl start`

- Stoppe den Apache Daemon:

`sudo apache2ctl stop`

- Starte den Apache Daemon neu:

`sudo apache2ctl restart`

- Überprüfe die syntax einer Konfigurationsdatei:

`sudo apache2ctl -t`

- Liste alle geladenen Module auf:

`sudo apache2ctl -M`
