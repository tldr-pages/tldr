# aws ecr

> Enviar, buscar, e gerenciar imagens de container.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- Autentica o Docker com o registro default (nome do usuário na AWS):

`aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`

- Cria um repositório:

`aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}`

- Cria uma tag em uma imagem local para o ECR:

`docker tag {{nome_do_container}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{nome_do_container}}:{{tag}}`

- Envia uma imagem para um repositório:

`docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{nome_do_container}}:{{tag}}`

- Busca a imagem de um repositório:

`docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{nome_do_container}}:{{tag}}`

- Apaga uma imagem de um repositório:

`aws ecr batch-delete-image --repository-name {{repositório}} --image-ids imageTag={{latest}}`

- Apaga um repositório:

`aws ecr delete-repository --repository-name {{repositório}} --force`

- Lista as imagens de um repositório:

`aws ecr list-images --repository-name {{repositório}}`
