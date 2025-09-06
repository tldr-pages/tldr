# aws-google-auth

> Outil en ligne de commande pour obtenir des credentials AWS temporaire (STS) en utilisant Google Apps comme un fournisseur de fédération (SSO).
> Plus d'informations : <https://github.com/cevoaustralia/aws-google-auth>.

- Connecte l'utilisateur avec le SSO Google en utilisant les identifiants IDP et SP et donne une durée de vie d'une heure à la connection :

`aws-google-auth -u {{exemple@exemple.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}}`

- Connecte l'utilisateur en lui demandant quel rôle utiliser (dans le cas où il y a plusieurs rôles SAML) :

`aws-google-auth -u {{exemple@exemple.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a`

- Résous les alias pour des comptes AWS :

`aws-google-auth -u {{exemple@exemple.com}} -I {{$GOOGLE_IDP_ID}} -S {{$GOOGLE_SP_ID}} -d {{3600}} -a --resolve-aliases`

- Affiche l'aide :

`aws-google-auth -h`
