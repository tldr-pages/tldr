# dirsearch

> Scaner cale web.
> Mai multe informaţii: <https://github.com/maurosoria/dirsearch>

- Scanați un server web pentru căi comune cu extensii comune:

`dirsearch --url {{url}} --extensions-list`

- Scanați o listă de servere web pentru căi comune cu extensia `.php:

`dirsearch --url-list {{path/to/url-list.txt}} --extensions {{php}}`

- Scanați un server web pentru căi definite de utilizator cu extensii comune:

`dirsearch --url {{url}} --extensions-list --wordlist {{path/to/url-paths.txt}}`

- Scanarea unui server web folosind un cookie:

`dirsearch --url {{url}} --extensions {{php}} --cookie {{cookie}}`

- Scanarea unui server web folosind metoda HTTP `HTTP:

`dirsearch --url {{url}} --extensions {{php}} --http-method {{HEAD}}`

- Scanați un server web, salvând rezultatele într-un fișier `.json`:

`dirsearch --url {{url}} --extensions {{php}} --json-report {{path/to/report.json}}`
