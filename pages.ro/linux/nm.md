# nm

> Listează numele simbolurilor în fișierele obiect.

- Lista funcțiilor globale (externe) într-un fișier (prefixat cu T):

`nm -g {{file.o}}`

- Listează numai simboluri nedefinite într-un fișier:

`nm -u {{file.o}}`

- Listează toate simbolurile, chiar și simbolurile de depanare:

`nm -a {{file.o}}`

- Demangle C++ simboluri (le face ușor de citit):

`nm --demangle {{file.o}}`
