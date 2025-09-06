# gobuster

> Findet versteckte Pfade auf Webservern und mehr.
> Weitere Informationen: <https://github.com/OJ/gobuster#modes>.

- Finde Verzeichnisse und Dateien, die den Wörtern der Wortliste entsprechen:

`gobuster dir {{[-u|--url]}} {{https://beispiel.com/}} {{[-w|--wordlist]}} {{pfad/zu/datei}}`

- Finde Subdomains:

`gobuster dns {{[-d|--domain]}} {{beispiel.com}} {{[-w|--wordlist]}} {{pfad/zu/datei}}`

- Finde Amazon S3-Buckets:

`gobuster s3 {{[-w|--wordlist]}} {{pfad/zu/datei}}`

- Finde andere virtuelle Hosts eines Servers:

`gobuster vhost {{[-u|--url]}} {{https://beispiel.com/}} {{[-w|--wordlist]}} {{pfad/zu/datei}}`

- Fuzze den Wert eines URL-Parameters:

`gobuster fuzz {{[-u|--url]}} {{https://beispiel.com/?parameter=FUZZ}} {{[-w|--wordlist]}} {{pfad/zu/datei}}`

- Fuzze den Namen eines URL-Parameters:

`gobuster fuzz {{[-u|--url]}} {{https://beispiel.com/?FUZZ=wert}} {{[-w|--wordlist]}} {{pfad/zu/datei}}`
