# aws

> La CLI officielle pour Amazon Web Services.
> Certaines commandes comme `aws s3` ont leur propre documentation.
> Plus d'informations : <https://aws.amazon.com/cli>.

- Configure la ligne de commande AWS :

`aws configure wizard`

- Configure la ligne de commande AWS en utilisant le SSO :

`aws configure sso`

- Voir l'aide pour une commande AWS :

`aws {{commande}} help`

- Récupère l'identité de l'appelant (utilisé pour débogguer les permissions) :

`aws sts get-caller-identity`

- Liste les ressources AWS d'une région et affiche le résultat en YAML :

`aws dynamodb list-tables --region {{us-east-1}} --output yaml`

- Utilise l'aide automatique au remplissage d'une commande :

`aws iam create-user --cli-auto-prompt`

- Utilise un guide interactif pour une ressource AWS :

`aws dynamodb wizard {{nouvelle_table}}`

- Génère un squelette CLI en JSON (utile pour l'Infrastructure as Code) :

`aws dynamodb update-table --generate-cli-skeleton`
