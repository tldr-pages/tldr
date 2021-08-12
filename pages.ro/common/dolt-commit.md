# dolt commit

> Comite modificări pe etape în tabele.
> Mai multe informaţii: <https://docs.dolthub.com/interfaces/cli#dolt-commit>

- Comite toate modificările pe etape, deschizând editorul specificat de `$EDITOR' pentru a introduce mesajul de comitere:

`dolt commit`

- Comite toate modificările pe etape cu mesajul specificat:

`dolt commit --message "{{commit_message}}"`

- Etapa toate modificările neetapizate la tabele înainte de a comite:

`dolt commit --all`

- Utilizaţi data de angajare specificată ISO 8601 (valorile implicite ale datei şi orei curente):

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- Utilizați autorul specificat pentru comiterea:

`dolt commit --author "{{author_name}} <{{author_email}}>"`

- Permite crearea unei comisiuni goale, fără modificări:

`dolt commit --allow-empty`

- Ignoră avertismentele cheie străine:

`dolt commit --force`
