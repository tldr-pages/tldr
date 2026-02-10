# aws ecr

> Push, pull e gestisce immagini container.
> Maggiori informazioni: <https://docs.aws.amazon.com/cli/latest/reference/ecr/>.

- Autentica Docker con il registro predefinito (username è AWS):

`aws ecr get-login-password --region {{regione}} | {{docker login}} --username AWS --password-stdin {{id_account_aws}}.dkr.ecr.{{regione}}.amazonaws.com`

- Crea un repository:

`aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{regione}}`

- Tagga un'immagine locale per ECR:

`docker tag {{nome_container}}:{{tag}} {{id_account_aws}}.dkr.ecr.{{regione}}.amazonaws.com/{{nome_container}}:{{tag}}`

- Push di un'immagine in un repository:

`docker push {{id_account_aws}}.dkr.ecr.{{regione}}.amazonaws.com/{{nome_container}}:{{tag}}`

- Pull di un'immagine da un repository:

`docker pull {{id_account_aws}}.dkr.ecr.{{regione}}.amazonaws.com/{{nome_container}}:{{tag}}`

- Elimina un'immagine da un repository:

`aws ecr batch-delete-image --repository-name {{repository}} --image-ids imageTag={{latest}}`

- Elimina un repository:

`aws ecr delete-repository --repository-name {{repository}} --force`

- Elenca le immagini all'interno di un repository:

`aws ecr list-images --repository-name {{repository}}`
