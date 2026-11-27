# aws s3

> CLI pour AWS S3 - fournit du stockage à travers des interfaces de services web.
> Certaines sous-commandes, telles que `cp`, disposent de leur propre documentation d'utilisation.
> Plus d'informations : <https://docs.aws.amazon.com/cli/latest/reference/s3/>.

- Affiche les fichiers d'un bucket :

`aws s3 ls {{nom_bucket}}`

- Synchronise les fichiers dans un répertoire local vers un bucket :

`aws s3 sync {{chemin/vers/répertoire}} s3://{{nom_bucket}}`

- Synchronise les fichiers et répertoires d'un bucket vers un répertoire local :

`aws s3 sync s3://{{nom_bucket}} {{chemin/vers/cible}}`

- Synchronise les fichiers dans un répertoire avec des exclusions :

`aws s3 sync {{chemin/vers/répertoire}} s3://{{nom_bucket}} --exclude {{chemin/vers/fichier}} --exclude {{chemin/vers/répertoire}}/*`

- Supprime un fichier d'un bucket :

`aws s3 rm s3://{{bucket}}/{{chemin/vers/fichier}}`

- Simule une commande sans apporter de modifications :

`aws s3 {{commande}} --dryrun`
