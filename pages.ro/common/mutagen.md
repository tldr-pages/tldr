# mutagen

> Instrumentul de sincronizare a fișierelor în timp real și redirecționare a rețelei.
> Mai multe informaţii: <https://mutagen.io>

- Începeți o sesiune de sincronizare între un director local și o gazdă la distanță:

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} {{user}}@{{host}}:{{/path/to/remote/directory/}}`

- Începeți o sesiune de sincronizare între un director local și un container Docker:

`mutagen sync create --name={{session_name}} {{/path/to/local/directory/}} docker://{{user}}@{{container_name}}{{/path/to/remote/directory/}}`

- Opriți o sesiune de alergare:

`mutagen sync terminate {{session_name}}`

- Începe un proiect:

`mutagen project start`

- Opriţi un proiect:

`mutagen project terminate`

- Lista sesiunilor de execuție pentru proiectul curent:

`mutagen project list`
