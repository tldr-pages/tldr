# aws ecr

> Konténerképek tolása, húzása és kezelése. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- Hitelesítse a Dockert az alapértelmezett regisztrációs rendszerrel (felhasználónév: AWS):

`aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`

- Hozzon létre egy tárolót:

`aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}`

- Jelöljön meg egy helyi képet az ECR számára:

`docker tag {{container_name}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Push egy képet egy tárolóba:

`docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Húzza ki a képet egy tárolóból:

`docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Kép törlése egy tárolóból:

`aws ecr batch-delete-image --repository-name {{repository}} --image-ids imageTag={{latest}}`

- Adattár törlése:

`aws ecr delete-repository --repository-name {{repository}} --force`

- Képek listázása egy adattárban:

`aws ecr list-images --repository-name {{repository}}`
