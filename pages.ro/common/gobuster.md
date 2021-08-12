# gobuster

> Forțează brutal căi ascunse pe serverele web și multe altele.
> Mai multe informaţii: <https://github.com/OJ/gobuster>

- Descoperiți directoarele și fișierele care se potrivesc în lista de cuvinte:

`gobuster dir --url {{https://example.com/}} --wordlist {{path/to/file}}`

- Descoperă subdomenii:

`gobuster dns --domain {{example.com}} --wordlist {{path/to/file}}`

- Descopera cupe Amazon S3:

`gobuster s3 --wordlist {{path/to/file}}`

- Descoperiți alte gazde virtuale pe server:

`gobuster vhost --url {{https://example.com/}} --wordlist {{path/to/file}}`

- Fuzz valoarea unui parametru:

`gobuster fuzz --url {{https://example.com/?parameter=FUZZ}} --wordlist {{path/to/file}}`

- Fuzz numele unui parametru:

`gobuster fuzz --url {{https://example.com/?FUZZ=value}} --wordlist {{path/to/file}}`
