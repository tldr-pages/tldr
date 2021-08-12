# aws ecr

> Apăsați, trageți și gestionați imagini container.
> Mai multe informaţii: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>

- Autentificați Docker cu registrul implicit (numele de utilizator este AWS):

`aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`

- Creați un depozit:

`aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}`

- Etichetați o imagine locală pentru ECR:

`docker tag {{container_name}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Împingeți o imagine într-un depozit:

`docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Trage o imagine dintr-un depozit:

`docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Ștergeți o imagine dintr-un depozit:

`aws ecr batch-delete-image  --repository-name {{repository}} --image-ids imageTag={{latest}}`

- Ștergeți un depozit:

`aws ecr delete-repository --repository-name {{repository}} --force`

- Lista imaginilor dintr-un depozit:

`aws ecr list-images --repository-name {{repository}}`
