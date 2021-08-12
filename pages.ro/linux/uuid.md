# uuid

> Generați și decodificați identificatori universale unice (UUID).
> A se vedea, de asemenea, `uuidgen”.
> Mai multe informaţii: <https://manned.org/uuid>

- Generează un UUIDv1 (pe baza timpului și a adresei hardware a sistemului, dacă este prezent):

`uuid`

- Generează un UUIDv4 (bazat pe date aleatorii):

`uuid -v {{4}}`

- Generați mai mulți identificatori UUIDv4 simultan:

`uuid -v {{4}} -n {{number_of_uuids}}`

- Generați un UIDv4 și specificați formatul de ieșire:

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- Generați un UUIDv4 și scrieți ieșirea într-un fișier:

`uuid -v {{4}} -o {{path/to/file}}`

- Generează un UUIDv5 (bazat pe numele obiectului furnizat) cu un prefix de nume specificat:

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{object_name}}`

- decodează un UUID dat:

`uuid -d {{uuid}}`
