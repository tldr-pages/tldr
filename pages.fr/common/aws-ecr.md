# aws ecr

> Pousse, récupère et gère les images de conteneur.
> Plus d'informations : <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- Connecte Docker avec le registre par défaut (le nom d'utilisateur est AWS) :

`aws ecr get-login-password --region {{région}} | {{docker login}} --username AWS --password-stdin {{id_de_compte_aws}}.dkr.ecr.{{région}}.amazonaws.com`

- Crée un dépôt :

`aws ecr create-repository --repository-name {{dépôt}} --image-scanning-configuration scanOnPush={{true|false}} --region {{région}}`

- Tag une image locale pour ECR :

`docker tag {{nom_de_conteneur}}:{{tag}} {{id_de_compte_aws}}.dkr.ecr.{{région}}.amazonaws.com/{{nom_de_conteneur}}:{{tag}}`

- Pousse une image dans le dépôt :

`docker push {{id_de_compte_aws}}.dkr.ecr.{{région}}.amazonaws.com/{{nom_de_conteneur}}:{{tag}}`

- Récupère une image depuis un dépôt :

`docker pull {{id_de_compte_aws}}.dkr.ecr.{{région}}.amazonaws.com/{{nom_de_conteneur}}:{{tag}}`

- Supprime une image d'un dépôt :

`aws ecr batch-delete-image --repository-name {{dépôt}} --image-ids imageTag={{latest}}`

- Supprime un dépôt :

`aws ecr delete-repository --repository-name {{dépôt}} --force`

- Liste les images dans un dépôt :

`aws ecr list-images --repository-name {{dépôt}}`
