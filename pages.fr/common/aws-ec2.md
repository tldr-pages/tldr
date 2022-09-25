# aws ec2

> CLI pour AWS EC2.
> Provisionne, sécurise et des capacités de calcul redimensionnable dans le cloud AWS pour accélérer le développement et le déploiement d'applications.
> Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ec2/index.html>.

- Affiche les informations sur une instance spécifique :

`aws ec2 describe-instances --instance-ids {{id_d_instance}}`

- Affiche les informations de toutes les instances :

`aws ec2 describe-instances`

- Affiche les informations sur tous les volumes EC2 :

`aws ec2 describe-volumes`

- Supprime un volume EC2 :

`aws ec2 delete-volume --volume-id {{id_de_volume}}`

- Crée une sauvegarde de votre volume EC2 :

`aws ec2 create-snapshot --volume-id {{id_de_volume}}`

- Liste toutes les AMIs (Images de Machine Amazon) disponible :

`aws ec2 describe-images`

- Affiche la liste de toutes les commandes EC2 disponible :

`aws ec2 help`

- Affiche l'aide pour une sous-commande EC2 spécifique :

`aws ec2 {{sous-commande}} help`
