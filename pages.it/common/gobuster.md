# gobuster

> Forza brute percorsi nascosti sui web server e altro.
> Maggiori informazioni: <https://github.com/OJ/gobuster#modes>.

- Scopre directory e file che corrispondono nella wordlist:

`gobuster dir {{[-u|--url]}} {{https://example.com/}} {{[-w|--wordlist]}} {{percorso/del/file}}`

- Scopre sottodomini:

`gobuster dns {{[-d|--domain]}} {{example.com}} {{[-w|--wordlist]}} {{percorso/del/file}}`

- Scopre bucket Amazon S3:

`gobuster s3 {{[-w|--wordlist]}} {{percorso/del/file}}`

- Scopre altri virtual host sul server:

`gobuster vhost {{[-u|--url]}} {{https://example.com/}} {{[-w|--wordlist]}} {{percorso/del/file}}`

- Fuzz il valore di un parametro:

`gobuster fuzz {{[-u|--url]}} {{https://example.com/?parameter=FUZZ}} {{[-w|--wordlist]}} {{percorso/del/file}}`

- Fuzz il nome di un parametro:

`gobuster fuzz {{[-u|--url]}} {{https://example.com/?FUZZ=value}} {{[-w|--wordlist]}} {{percorso/del/file}}`
