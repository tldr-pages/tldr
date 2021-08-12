# darkhttpd

> server web Darkhttpd.
> Mai multe informaţii: <https://unix4lyfe.org/darkhttpd>

- Porniți serverul care deservește rădăcina documentului specificat:

`darkhttpd {{path/to/docroot}}`

- Porniți serverul pe portul specificat (portul 8080 implicit dacă rulează ca utilizator non-root):

`darkhttpd {{path/to/docroot}} --port {{port}}`

- Ascultați numai pe adresa IP specificată (în mod implicit, serverul ascultă pe toate interfețele):

`darkhttpd {{path/to/docroot}} --addr {{ip_address}}`
