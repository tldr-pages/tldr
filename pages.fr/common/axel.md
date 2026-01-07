# axel

> Accélérateur de téléchargement.
> Supporte HTTP, HTTPS, et FTP.
> Voir aussi : `aria2c`.
> Plus d'informations : <https://manned.org/axel>.

- Télécharge depuis une URL vers un fichier :

`axel {{url}}`

- Télécharge et spécifie le nom de fichier :

`axel {{url}} {{[-o|--output]}} {{chemin/vers/fichier}}`

- Télécharge avec plusieurs connections :

`axel {{[-n|--num-connections]}} {{nombre_de_connections}} {{url}}`

- Recherche des miroirs :

`axel {{[-S|--search=]}}{{nombre_de_miroirs}} {{url}}`

- Limite la vitesse de téléchargement (en octets par secondes) :

`axel {{[-s|--max-speed]}} {{vitesse}} {{url}}`
