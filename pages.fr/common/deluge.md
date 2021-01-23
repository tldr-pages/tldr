# deluge

> Client BitTorrent à base de ligne de commande.
> Plus d'informations : <https://deluge-torrent.org>.

- Télécharge un torrent :

`deluge {{url|magnet|chemin/vers/fichier}}`

- Télécharge un torrent à l'aide d'un fichier de configuration particulier :

`deluge -c {{chemin/vers/fichier_configuration}} {{url|magnet|chemin/vers/fichier}}`

- Télécharge un torrent et lance un interface usager particulier :

`deluge -u {{gtk|web|console}} {{url|magnet|chemin/vers/fichier}}`

- Télécharge un torrent et enregistre les journaux dans un ficher :

`deluge -l {{chemin/vers/fichier_journalisation}} {{url|magnet|chemin/vers/fichier}}`
