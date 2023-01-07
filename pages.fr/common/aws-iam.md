# aws iam

> CLI pour AWS IAM.
> Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/iam/index.html>.

- Affiche la page d'aide pour `aws iam` (avec toutes les commandes iam disponibles) :

`aws iam help`

- Liste les utilisateurs :

`aws iam list-users`

- Liste les politiques :

`aws iam list-policies`

- Liste les groupes :

`aws iam list-groups`

- Récupère les utilisateurs dans un groupe :

`aws iam get-group --group-name {{nom_du_groupe}}`

- Décris une politique IAM :

`aws iam get-policy --policy-arn arn:aws:iam::aws:policy/{{nom_de_la_politique}}`

- Liste les clés d’accès :

`aws iam list-access-keys`

- Liste les clés d'accès pour un utilisateur spécifique :

`aws iam list-access-keys --user-name {{nom_d_utilisateur}}`
