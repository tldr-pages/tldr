# axel

> Accélérateur de téléchargement.
> Supporte HTTP, HTTPS, et FTP.
> Plus d'informations : <https://github.com/axel-download-accelerator/axel>.

- Télécharge depuis une URL vers un fichier :

`axel {{url}}`

- Télécharge et spécifie le nom de fichier :

`axel {{url}} -o {{nom_de_fichier}}`

- Télécharge avec plusieurs connections :

`axel -n {{nombre_de_connections}} {{url}}`

- Recherche des miroirs :

`axel -S {{nombre_de_miroirs}} {{url}}`

- Limite la vitesse de téléchargement (en octets par secondes) :

`axel -s {{vitesse}} {{url}}`
