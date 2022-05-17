# ab

> Outil d'analyse pour serveur Apache HTTP.
> Plus d'informations : <https://httpd.apache.org/docs/current/programs/ab.html>.

- Exécute 100 requêtes HTTP GET sur une URL donnée :

`ab -n {{100}} {{url}}`

- Exécute 100 requêtes HTTP GET en parallèle par groupe de 10, sur une URL :

`ab -n {{100}} -c {{10}} {{url}}`

- Exécute 100 requêtes HTTP POST sur une URL, en utilisant un contenu JSON depuis un fichier :

`ab -n {{100}} -T {{application/json}} -p {{chemin/vers/le/fichier.json}} {{url}}`

- Utilise la fonctionalitée HTTP Keep Alive pour exécuter plusieurs requêtes dans la même session HTTP :

`ab -k {{url}}`

- Fixe le nombre maximum de secondes d'exécution pour l'analyse :

`ab -t {{60}} {{url}}`
