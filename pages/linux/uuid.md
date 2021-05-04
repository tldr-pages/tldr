# uuid

> Generate and decode an Universally Unique Identifier (UUID).
> More information: <https://manned.org/uuid.1>.

- Generate a v1 UUID (time and node based):

`uuid`

- Generate a v4 UUID (random data based):

`uuid -v {{4}}`

- Generate a v3 UUID (name based) with an URL namespace:

`uuid -v {{3}} ns:URL {{https://example.com}}`

- Generate multiple v1 UUIDs at once by specifying a count:

`uuid -n {{12}}`

- Generate a v1 UUID in a single integer value (SIV) representation format:

`uuid -F {{SIV}}`

- Generate a v1 UUID and write the output to a file:

`uuid -o {{path/to/file}}`

- Decode a given UUID:

`uuid -d {{68794df6-5e20-385f-ab08-bb73f8a433cb}}`
