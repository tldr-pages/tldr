# mongorestore

> Utilitate pentru a importa o colecție sau o bază de date dintr-o imagine binară într-o instanță MongoDB.
> Mai multe informaţii: <https://docs.mongodb.com/database-tools/mongorestore/>

- Importați o imagine de date bson dintr-un director într-o bază de date MongoDB:

`mongorestore --db {{database_name}} {{path/to/directory}}`

- Importați o imagine de date bson dintr-un director într-o bază de date dată într-o gazdă de server MongoDB, care rulează într-un anumit port, cu autentificare utilizator (utilizatorul va fi solicitat pentru parolă):

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/directory}} --password`

- Importați o colecție dintr-un fișier bson într-o bază de date MongoDB:

`mongorestore --db {{database_name}} {{path/to/file}}`

- Importați o colecție dintr-un fișier bson într-o bază de date dată într-o gazdă de server MongoDB, care rulează într-un anumit port, cu autentificarea utilizatorului (utilizatorul va fi solicitat pentru parolă):

`mongorestore --host {{database_host:port}} --db {{database_name}} --username {{username}} {{path/to/file}} --password`
