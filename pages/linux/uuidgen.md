# uuidgen

> Generate unique identifiers (UUIDs).
> See also `uuid`.
> More information: <https://manned.org/uuidgen>.

- Create a random UUIDv4:

`uuidgen {{[-r|--random]}}`

- Create a UUIDv1 based on the current time:

`uuidgen {{[-t|--time]}}`

- Create a UUIDv5 of the name with a specified namespace prefix:

`uuidgen {{[-s|--sha1]}} {{[-n|--namespace]}} {{@dns|@url|@oid|@x500}} {{[-N|--name]}} {{object_name}}`
