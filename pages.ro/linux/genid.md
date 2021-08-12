# genid

> Generați ID-uri, cum ar fi fulgi de zăpadă, UUID-uri și un nou GAID.
> Mai multe informaţii: <https://github.com/bleonard252/genid>

- Generează un UUIDv4:

`genid uuid`

- Generați un UUIDv5 utilizând un UUID de spațiu de nume și un nume specific:

`genid uuidv5 {{{ce598faa-8dd0-49ee-8525-9e24fff71dca}}} {{name}}`

- Generează o discordie fulg de nea, fără o linie nouă (utilă în scripturi shell):

`genid --script snowflake`

- Generează un ID anonim generic cu un anumit „ID real”:

`genid gaid {{real_id}}`

- Generează un fulg de nea cu epoca stabilită la o anumită dată:

`genid snowflake --epoch={{unix_epoch_time}}`
