# mongodump

> Utilitate pentru a exporta conținutul unei instanțe MongoDB.
> Mai multe informaţii: <https://docs.mongodb.com/database-tools/mongodump/>

- Creați o imagine de memorie a tuturor bazelor de date (acest lucru va plasa fișierele într-un director numit „dump”):

`mongodump`

- Specificați o locație de ieșire pentru dump:

`mongodump --out {{path/to/directory}}`

- Creați o imagine de memorie a unei baze de date date:

`mongodump --db {{database_name}}`

- Creați o imagine de memorie a unei anumite colecții într-o anumită bază de date:

`mongodump --collection {{collection_name}} --db {{database_name}}`

- Conectați-vă la o gazdă dată care rulează pe un anumit port și creați o imagine de memorie:

`mongodump --host {{host}} --port {{port}}`

- Creați o imagine de memorie a unei baze de date date cu un anumit nume de utilizator; utilizatorul va fi solicitat pentru parolă:

`mongodump --username {{username}} {{database}} --password`
