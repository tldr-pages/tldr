# uuidgen

> Stwórz unikalny identyfikator (UUIDs).
> Zobacz też `uuid`.
> Więcej informacji: <https://manned.org/uuidgen>.

- Stwórz losowy UUIDv4:

`uuidgen --random`

- Stwórz UUIDv1 oparty o aktualny czas:

`uuidgen --time`

- Stwórz UUIDv5 z nazwy i prefiksu przestrzeni nazw:

`uuidgen --sha1 --namespace {{@dns|@url|@oid|@x500}} --name {{nazwa_obiektu}}`
