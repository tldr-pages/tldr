# gobuster

> Findet versteckte Pfade auf Webservern und mehr.
> Weitere Informationen: <https://github.com/OJ/gobuster>.

- Finde Verzeichnisse und Dateien, die den Wörtern der Wortliste entsprechen.

`gobuster dir --url {{https://beispiel.com/}} --wordlist {{pfad/zu/datei}}`

- Finde Subdomains:

`gobuster dns --domain {{beispiel.com}} --wordlist {{pfad/zu/datei}}`

- Finde Amazon S3-Buckets:

`gobuster s3 --wordlist {{pfad/zu/datei}}`

- Finde andere virtuelle Hosts eines Servers:

`gobuster vhost --url {{https://beispiel.com/}} --wordlist {{pfad/zu/datei}}`

- Fuzze den Wert eines URL-Parameters:

`gobuster fuzz --url {{https://beispiel.com/?parameter=FUZZ}} --wordlist {{pfad/zu/datei}}`

- Fuzze den Namen eines URL-Parameters

`gobuster fuzz --url {{https://beispiel.com/?FUZZ=wert}} --wordlist {{pfad/zu/datei}}`
