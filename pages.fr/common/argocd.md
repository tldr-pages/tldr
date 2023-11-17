# argocd

> Interface en ligne de commande pour controler un serveur Argo CD.
> Certaines sous-commandes comme `argocd app` ont leur propre documentation d'utilisation.
> Plus d'informations : <https://argo-cd.readthedocs.io/en/stable/user-guide/commands/argocd/>.

- Se connecter à un serveur Argo CD :

`argocd login --insecure --username {{utilisateur}} --password {{mot_de_passe}} {{serveur_argocd:port}}`

- Liste des applications :

`argocd app list`
