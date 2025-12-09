# sysctl

> Liste et modifie les variables d'exécution du noyau.
> Plus d'informations : <https://manned.org/sysctl.8>.

- Affiche toutes les variables disponibles et leurs valeurs :

`sysctl -a`

- Définis une variable d'état modifiable du noyau :

`sysctl -w {{section.modifiable}}={{valeur}}`

- Obtiens les gestionnaires de fichiers (handlers) actuellement ouverts :

`sysctl fs.file-nr`

- Obtiens la limite de nombre de fichiers ouverts simultanément :

`sysctl fs.file-max`

- Applique les changements de `/etc/sysctl.conf` :

`sysctl -p`
