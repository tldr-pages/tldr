# curl

> Transfère des données depuis ou vers un serveur.
> Accepte la plupart des protocoles, notamment HTTP, FTP et POP3.
> Plus d'informations : <https://curl.se/docs/manpage.html>.

- Télécharger le contenu d'une URL dans un fichier :

`curl {{http://exemple.fr}} {{[-o|--output]}} {{nom_fichier}}`

- Télécharger le contenu d'une URL dans un fichier nommé comme indiqué par l'URL :

`curl {{[-O|--remote-name]}} {{http://exemple.fr/nom_fichier}}`

- Télécharger un fichier, en suivant les redirections, et poursuivre (reprendre) automatiquement un transfert de fichier précédent et renvoyer une erreur lors d'erreurs serveurs :

`curl {{[-f|--fail]}} {{[-O|--remote-name]}} {{[-L|--location]}} {{[-C|--continue-at]}} - {{http://exemple.fr/nom_fichier}}`

- Envoyer des données de formulaire encodées (requête POST de type `application/x-www-form-urlencoded`). Utiliser `--data @file_name` ou `--data @'-'` pour lire depuis `stdin` :

`curl {{[-d|--data]}} {{'nom=bob'}} {{http://exemple.fr/formulaire}}`

- Envoyer une requête avec un en-tête supplémentaire, en spécifiant la méthode HTTP :

`curl {{[-H|--header]}} {{'X-Mon-En-Tete: 123'}} {{[-X|--request]}} {{PUT}} {{http://exemple.fr}}`

- Envoyez des données au format JSON, en spécifiant l'en-tête content-type adéquate :

`curl {{[-d|--data]}} {{'{"nom":"bob"}'}} {{[-H|--header]}} {{'Content-Type: application/json'}} {{http://exemple.fr/utilisateurs/1234}}`

- Fournir un nom d'utilisateur et demander pour un mot de passe pour une authentification auprès du serveur :

`curl {{[-u|--user]}} {{identifiant}} {{http://exemple.fr}}`

- Fournir le certificat et la clé du client pour une ressource, en évitant la validation du certificat :

`curl {{[-E|--cert]}} {{client.pem}} --key {{cle.pem}} {{[-k|--insecure]}} {{https://exemple.fr}}`
