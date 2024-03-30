# genid

> Generate IDs, such as snowflakes, UUIDs, and a new GAID.
> More information: <https://github.com/bleonard252/genid>.

- Generate a UUIDv4:

`genid uuid`

- Generate a UUIDv5 using a namespace UUID and a specific name:

`genid uuidv5 {{ce598faa-8dd0-49ee-8525-9e24fff71dca}} {{name}}`

- Generate a Discord Snowflake, without a trailing newline (useful in shell scripts):

`genid --script snowflake`

- Generate a Generic Anonymous ID with a specific "real ID":

`genid gaid {{real_id}}`

- Generate a Snowflake with the epoch set to a specific date:

`genid snowflake --epoch={{unix_epoch_time}}`
