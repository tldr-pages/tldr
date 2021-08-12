# wpscan

> Scaner de vulnerabilitate WordPress.
> Mai multe informaţii: <https://github.com/wpscanteam/wpscan>

- Actualizați baza de date de vulnerabilitate:

`wpscan --update`

- Scanați un site WordPress:

`wpscan --url {{url}}`

- Scanați un site WordPress, folosind agenți de utilizator aleatoare și detectarea pasivă:

`wpscan --url {{url}} --stealthy`

- Scanați un site web WordPress, verificând pluginurile vulnerabile și specificând calea către directorul `wp-content`:

`wpscan --url {{url}} --enumerate {{vp}} --wp-content-dir {{remote/path/to/wp-content}}`

- Scanați un site web WordPress printr-un proxy:

`wpscan --url {{url}} --proxy {{protocol://ip:port}} --proxy-auth {{username:password}}`

- Efectuați enumerarea identificatorilor de utilizator pe un site web WordPress:

`wpscan --url {{url}} --enumerate {{u}}`

- Executați un atac de ghicitul parolei pe un site WordPress:

`wpscan --url {{url}} --usernames {{username|path/to/usernames.txt}} --passwords {{path/to/passwords.txt}} threads {{20}}`

- Scanați un site WordPress, colectarea datelor de vulnerabilitate din WPvulnDB (https://wpvulndb.com/):

`wpscan --url {{url}} --api-token {{token}}`
