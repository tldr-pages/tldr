# aws s3

> CLI pour AWS S3 - fournis du stockage à travers les services web.
> Certaines sous-commandes, telles que `cp`, disposent de leur propre documentation d'utilisation.
> Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/s3/>.

- Affiche les fichiers d'un bucket :

`aws s3 ls {{nom_bucket}}`

- Synchronise les fichiers et répertoires locaux avec un bucket :

`aws s3 sync {{chemin/vers/fichiers}} s3://{{nom_bucket}}`

- Synchronise les fichiers et répertoires d'un bucket avec le ceux en local :

`aws s3 sync s3://{{nom_bucket}} {{chemin/vers/cible}}`

- Synchronise les fichiers et les répertoires avec des exclusions :

`aws s3 sync {{chemin/vers/fichiers}} s3://{{nom_bucket}} --exclude {{chemin/vers/fichier}} --exclude {{chemin/vers/répertoire}}/*`

- Supprime un fichier d'un bucket :

`aws s3 rm s3://{{bucket}}/{{chemin/vers/fichier}}`

- Prévisualise uniquement les changements :

`aws s3 {{commande}} --dryrun`
