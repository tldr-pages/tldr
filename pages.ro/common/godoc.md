# godoc

> Afișați documentația pentru pachetele go.
> Mai multe informaţii: <https://godoc.org/>

- Afișează ajutor pentru pachetul „fmt”:

`godoc {{fmt}}`

- Afișează ajutor pentru funcția „Printf” a pachetului „fmt”:

`godoc {{fmt}} {{Printf}}`

- Serviți documentația ca server web pe portul 6060:

`godoc -http=:{{6060}}`

- Creați un fișier index:

`godoc -write_index -index_files={{path/to/file}}`

- Utilizați fișierul index dat pentru a căuta în documente:

`godoc -http=:{{6060}} -index -index_files={{path/to/file}}`
