# nm

> Az objektumfájlok szimbólumneveinek listázása. További információ: <https://manned.org/nm>.

- Globális (extern) függvények listázása egy fájlban (T előtaggal):

`nm -g {{path/to/file.o}}`

- Csak a nem definiált szimbólumok listázása egy fájlban:

`nm -u {{path/to/file.o}}`

- Az összes szimbólum listázása, még a hibakeresési szimbólumoké is:

`nm -a {{path/to/file.o}}`

- C++ szimbólumok szétválasztása (olvashatóvá tétele):

`nm --demangle {{path/to/file.o}}`
