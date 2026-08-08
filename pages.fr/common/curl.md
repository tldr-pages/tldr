# curl

> Transfère des données depuis ou vers un serveur.
> Accepte la plupart des protocoles, notamment HTTP, HTTPS, FTP, SCP, etc.
> Voir aussi : `wcurl`, `wget`.
> Plus d'informations : <https://curl.se/docs/manpage.html>.

- Faire une requête HTTP GET et afficher la réponse :

`curl {{http://example.com}}`

- Faire une requête HTTP GET, suivre toute redirection HTTP `3xx`, et afficher les en-têtes de la réponse :

`curl {{[-L|--location]}} {{[-D|--dump-header]}} - {{https://example.com}}`

- Télécharger le contenu d'une URL dans un fichier nommé comme indiqué par l'URL :

`curl {{[-O|--remote-name]}} {{http://example.com/nom_fichier.zip}}`

- Envoyer des données de formulaire encodées (requête POST de type `application/x-www-form-urlencoded`). Utiliser `--data @file_name` ou `--data @'-'` pour lire depuis `stdin` :

`curl {{[-d|--data]}} {{'nom=bob'}} {{http://example.com/formulaire}}`

- Envoyer une requête avec un en-tête supplémentaire, en spécifiant la méthode HTTP, à travers un proxy, et en ignorant les erreurs de validation de certificat :

`curl {{[-k|--insecure]}} {{[-x|--proxy]}} {{http://127.0.0.1:8080}} {{[-H|--header]}} '{{Authorization: Bearer token}}' {{[-X|--request]}} {{GET|PUT|POST|DELETE|PATCH|...}} {{https://example.com}}`

- Envoyer des données au format JSON, en spécifiant l'en-tête Content-Type adéquate :

`curl {{[-d|--data]}} {{'{"nom":"bob"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://example.com/utilisateurs/1234}}`

- Fournir le certificat et la clé privée du client pour l'accès à une URL :

`curl {{[-E|--cert]}} {{client.pem}} --key {{cle.pem}} {{https://example.com}}`

- Résoudre un nom de domaine vers une adresse IP spécifique (similaire à modifier le fichier /etc/hosts pour une résolution DNS locale), en activant le mode verbeux :

`curl {{[-v|--verbose]}} --resolve {{example.com}}:{{80}}:{{127.0.0.1}} {{http://example.com}}`
