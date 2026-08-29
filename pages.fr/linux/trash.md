# trash

> Gère la corbeille.
> Plus d’informations : <https://github.com/andreafrancia/trash-cli>.

- Envoie un fichier à la corbeille :

`trash {{chemin/vers/fichier}}`

- Liste tous les fichiers dans la corbeille :

`trash-list`

- Restaure interactivement un fichier depuis la corbeille :

`trash-restore`

- Vide la corbeille :

`trash-empty`

- Supprime définitivement tous les fichiers de la corbeille datant de plus de 10 jours :

`trash-empty 10`

- Supprime tous les fichiers de la corbeille qui correspondent à schéma d'expension de fichier :

`trash-rm "{{*.o}}"`

- Supprime tous les fichiers ayant un emplacement d’origine spécifique :

`trash-rm /{{chemin/vers/fichier_ou_dossier}}`
