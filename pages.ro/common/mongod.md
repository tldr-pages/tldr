# mongod

> Serverul de baze de date MongoDB.
> Mai multe informaţii: <https://docs.mongodb.com/manual/reference/program/mongod>

- Specificați un fișier de configurare:

`mongod --config {{filename}}`

- Specificați portul pe care doriți să-l ascultați:

`mongod --port {{port}}`

- Specificați nivelul de profilare a bazei de date. 0 este oprit, 1 este doar operațiuni lente, 2 este tot:

`mongod --profile {{0|1|2}}`
