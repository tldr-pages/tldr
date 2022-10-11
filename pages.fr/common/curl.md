# curl

> Transfère des données depuis ou vers un serveur.
> Accepte la plupart des protocoles, notamment HTTP, FTP et POP3.
> Plus d'informations : <https://curl.se>.

- Télécharger le contenu d'une URL dans un fichier :

`curl {{http://exemple.fr}} --output {{nom_fichier}}`

- Télécharger le contenu d'une URL dans un fichier nommé comme indiqué par l'URL :

`curl --remote-name {{http://exemple.fr/nom_fichier}}`

- Télécharger un fichier, en suivant les redirections, et poursuivre (reprendre) automatiquement un transfert de fichier précédent et renvoyer une erreur lors d'erreurs serveurs :

`curl --fail --remote-name --location --continue-at - {{http://exemple.fr/nom_fichier}}`

- Envoyer des données de formulaire encodées (requête POST de type `application/x-www-form-urlencoded`). Utiliser `--data @file_name` ou `--data @'-'` pour lire depuis STDIN :

`curl --data {{'nom=bob'}} {{http://exemple.fr/formulaire}}`

- Envoyer une requête avec un en-tête supplémentaire, en spécifiant la méthode HTTP :

`curl --header {{'X-Mon-En-Tete: 123'}} --request {{PUT}} {{http://exemple.fr}}`

- Envoyez des données au format JSON, en spécifiant l'en-tête content-type adéquate :

`curl --data {{'{"nom":"bob"}'}} --header {{'Content-Type: application/json'}} {{http://exemple.fr/utilisateurs/1234}}`

- Fournir un nom d'utilisateur et un mot de passe pour une authentification auprès du serveur :

`curl --user identifiant:motdepasse {{http://exemple.fr}}`

- Fournir le certificat et la clé du client pour une ressource, en évitant la validation du certificat :

`curl --cert {{client.pem}} --key {{cle.pem}} --insecure {{https://exemple.fr}}`
