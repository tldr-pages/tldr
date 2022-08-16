# aws cur

> Crée, requête et supprime des rapports de définition d'utilisation AWS.
> Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cur/index.html>.

- Créé un rapport de définition de coût et d'utilisation AWS depuis un fichier JSON :

`aws cur put-report-definition --report-definition file://{{chemin/vers/rapport_de_définition.json}}`

- Liste les rapports de définition définis pour le compte connecté :

`aws cur describe-report-definitions`

- Supprime un rapport de définition d'utilisation :

`aws cur --region {{region_aws}} delete-report-definition --report-name {{rapport}}`
