# uuid

> Generate and decode Universally Unique Identifiers (UUID).
> See also `uuidgen`.
> More information: <https://manned.org/uuid>.

- Generate a v1 UUID (based on time and system's hardware address, if present):

`uuid`

- Generate a v4 UUID (random data based):

`uuid -v {{4}}`

- Generate a v5 UUID (name based) with an URL namespace:

`uuid -v {{5}} ns:URL {{https://example.com}}`

- Generate multiple v1 UUIDs at once:

`uuid -n {{number_of_uuids}}`

- Generate a v1 UUID and specify the output format:

`uuid -F {{BIN|STR|SIV}}`

- Generate a v1 UUID and write the output to a file:

`uuid -o {{path/to/file}}`

- Decode a given UUID:

`uuid -d {{uuid}}`
