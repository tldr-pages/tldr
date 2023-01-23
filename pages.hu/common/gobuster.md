# gobuster

> Brutális erővel kényszeríti ki a rejtett elérési utakat a webszervereken és még sok minden mást. További információ: <https://github.com/OJ/gobuster>.

- A szólistában egyező könyvtárak és fájlok felfedezése:

`gobuster dir --url {{https://example.com/}} --wordlist {{path/to/file}}`

- Aldomainek felfedezése:

`gobuster dns --domain {{example.com}} --wordlist {{path/to/file}}`

- Amazon S3 vödrök felfedezése:

`gobuster s3 --wordlist {{path/to/file}}`

- Más virtuális hosztok felfedezése a szerveren:

`gobuster vhost --url {{https://example.com/}} --wordlist {{path/to/file}}`

- Fuzz egy paraméter értékét:

`gobuster fuzz --url {{https://example.com/?parameter=FUZZ}} --wordlist {{path/to/file}}`

- Fuzz a paraméter neve:

`gobuster fuzz --url {{https://example.com/?FUZZ=value}} --wordlist {{path/to/file}}`
