# base64

> Encoder ou décoder un fichier ou l'entrée standard en utilisant le codage Base64 à destination de la sortie standard.
> Plus d'informations : <https://www.gnu.org/software/coreutils/base64>.

- Encoder un fichier :

`base64 {{fichier}}`

- Décoder un fichier :

`base64 --decode {{fichier}}`

- Encoder depuis stdin :

`{{une_commande}} | base64`

- Décoder depuis stdin :

`{{une_commande}} | base64 --decode`
