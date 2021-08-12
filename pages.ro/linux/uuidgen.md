# uuidgen

> Generați identificatori unici (UUID).
> A se vedea, de asemenea, „uid”.
> Mai multe informaţii: <https://manned.org/uuidgen>

- Creați un UUIDv4 aleatoare:

`uuidgen --random`

- Creați un UUIDv1 bazat pe ora curentă:

`uuidgen --time`

- Creați un UUIDv5 al numelui cu un prefix de nume specificat:

`uuidgen --sha1 --namespace {{@dns|@url|@oid|@x500}} --name {{object_name}}`
