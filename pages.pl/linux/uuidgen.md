# uuidgen

> Stwórz unikalny identyfikator (UUIDs).
> Zobacz także: `uuid`.
> Więcej informacji: <https://manned.org/uuidgen>.

- Stwórz losowy UUIDv4:

`uuidgen {{[-r|--random]}}`

- Stwórz UUIDv1 oparty o aktualny czas:

`uuidgen {{[-t|--time]}}`

- Stwórz UUIDv5 z nazwy i prefiksu przestrzeni nazw:

`uuidgen {{[-s|--sha1]}} {{[-n|--namespace]}} {{@dns|@url|@oid|@x500}} {{[-N|--name]}} {{nazwa_obiektu}}`
