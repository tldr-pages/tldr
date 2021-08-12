# shiori

> Manager de marcaje simplu construit cu Go.
> Mai multe informaţii: <https://github.com/go-shiori/shiori>

- Importați semne de carte din fișierul format de marcaj HTML Netscape:

`shiori import {{path/to/bookmarks.html}}`

- Salvați adresa URL specificată ca semn de carte:

`shiori add {{url}}`

- Listați marcajele salvate:

`shiori print`

- Deschideți marcajul salvat într-un browser:

`shiori open {{bookmark_id}}`

- Porniți interfața web pentru gestionarea marcajelor la portul 8181:

`shiori serve --port {{8181}}`
