# sysctl

> Lister et modifier les variables d'exécution du noyau.

- Afficher toutes les variables disponibles et leurs valeurs :

`sysctl -a`

- Définir une variable d'état modifiable du noyau :

`sysctl -w {{section.modifiable}}={{valeur}}`

- Obtenir les gestionnaires de fichiers (handlers) actuellement ouverts :

`sysctl fs.file-nr`

- Obtenir la limite de nombre de fichiers ouverts simultanément :

`sysctl fs.file-max`

- Appliquer les changements de `/etc/sysctl.conf`:

`sysctl -p`
