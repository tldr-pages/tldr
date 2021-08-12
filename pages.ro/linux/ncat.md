# ncat

> Utilizați funcționalitatea normală `cat` în rețele.

- Ascultați intrarea pe portul specificat și scrieți-o în fișierul specificat:

`ncat -l {{port}} > {{path/to/file}}`

- Acceptaţi mai multe conexiuni şi păstraţi ncat deschis după ce au fost închise:

`ncat -lk {{port}}`

- Scrieți ieșirea fișierului specificat la gazda specificată pe portul specificat:

`ncat {{address}} {{port}} < {{path/to/file}}`
