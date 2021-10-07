# base64

> Encoder ou décoder un fichier ou l'entrée standard en utilisant le codage Base64 à destination de la sortie standard.
> Plus d'informations : <https://www.gnu.org/software/coreutils/base64>.

- Encode un fichier :

`base64 {{fichier}}`

- Décode un fichier :

`base64 --decode {{fichier}}`

- Encode depuis stdin :

`{{une_commande}} | base64`

- Décode depuis stdin :

`{{une_commande}} | base64 --decode`
