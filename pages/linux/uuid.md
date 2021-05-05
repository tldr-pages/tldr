# uuid

> Generate and decode Universally Unique Identifiers (UUID).
> See also `uuidgen`.
> More information: <https://manned.org/uuid>.

- Generate a UUIDv1 (based on time and system's hardware address, if present):

`uuid`

- Generate a UUIDv4 (based on random data):

`uuid -v {{4}}`

- Generate multiple UUIDv4 identifiers at once:

`uuid -v {{4}} -n {{number_of_uuids}}`

- Generate a UUIDv4 and specify the output format:

`uuid -v {{4}} -F {{BIN|STR|SIV}}`

- Generate a UUIDv4 and write the output to a file:

`uuid -v {{4}} -o {{path/to/file}}`

- Generate a UUIDv5 (based on the supplied object name) with a specified namespace prefix:

`uuid -v {{5}} ns:{{DNS|URL|OID|X500}} {{object_name}}`

- Decode a given UUID:

`uuid -d {{uuid}}`
