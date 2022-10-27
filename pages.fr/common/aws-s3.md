# aws s3

> CLI pour AWS S3 - fournis du stockage à travers les services web.
> Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/s3/index.html>.

- Affiche les fichiers d'un bucket :

`aws s3 ls {{nom_du_bucket}}`

- Synchronise les fichiers et dossiers locaux avec un bucket :

`aws s3 sync {{chemin/vers/les/fichiers}} s3://{{nom_du_bucket}}`

- Synchronise les fichiers et dossiers d'un bucket avec le ceux en local :

`aws s3 sync s3://{{nom_du_bucket}} {{chemin/vers/cible}}`

- Synchronise les fichiers et les dossiers avec des exclusions :

`aws s3 sync {{chemin/vers/les/fichiers}} s3://{{nom_du_bucket}} --exclude {{chemin/vers/le/fichier}} --exclude {{chemin/vers/le/dossier}}/*`

- Supprime un fichier d'un bucket :

`aws s3 rm s3://{{bucket}}/{{chemin/vers/le/fichier}}`

- Prévisualise uniquement les changements :

`aws s3 {{n_importe_quelle_commande}} --dryrun`
