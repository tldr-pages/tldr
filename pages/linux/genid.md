# genid

> Generate IDs, such as snowflakes, UUIDs, and a new GAID.
> More information: <https://github.com/bleonard252/genid>.

- Generate a UUIDv4:

`genid uuid`

- Generate a UUIDv5 with a namespace UUID and name THISISANAME:

`genid uuidv5 {{{ce598faa-8dd0-49ee-8525-9e24fff71dca}}} {{THISISANAME}}`

- Generate a Discord Snowflake, without a trailing newline (for scripts):

`genid --script snowflake`

- Generate a Generic Anonymous ID with "real ID" tldrpages:

`genid gaid {{tldrpages}}`

- Generate a Snowflake with the epoch set to March 13, 2020:

`genid snowflake --epoch={{1584072000}}`
