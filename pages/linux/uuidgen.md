# uuidgen

> Generate unique identifiers (UUIDs).
> See also `uuid`.
> More information: <https://manned.org/uuidgen>.

- Create a random v4 UUID:

`uuidgen --random`

- Create a v1 UUID based on the current time:

`uuidgen --time`

- Create a v5 UUID of the name with a specified namespace prefix:

`uuidgen --sha1 --namespace {{@dns|@url|@oid|@x500}} --name {{object_name}}`
