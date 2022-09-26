# apache2ctl

> Das CLI Tool um den Apache HTTP Web Server zu administrieren.
> Dieser Befehl wird mit Debian-basierten Betriebssystemen geliefert, für RHEL siehe `httpd`.
> Weitere Informationen: <https://manpages.debian.org/latest/apache2/apache2ctl.8.en.html>.

- Starte den Apache daemon. Gibt einen Fehler aus, wenn er bereits läuft:

`sudo apache2ctl start`

- Stoppe den Apache Daemon:

`sudo apache2ctl stop`

- Starte den Apache Daemon neu:

`sudo apache2ctl restart`

- Überprüfe die Syntax einer Konfigurationsdatei:

`sudo apache2ctl -t`

- Liste alle geladenen Module auf:

`sudo apache2ctl -M`
