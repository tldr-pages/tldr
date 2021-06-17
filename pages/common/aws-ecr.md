# aws ecr

> Push, pull, and manage container images.
> More information: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ecr/index.html>.

- Authenticate local container manager to your default registry (username is AWS):

`aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`

- Create a repository:

`aws ecr create-repository --repository-name {{repo_name}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}`

- Give your image an appropriate tag for ECR:

`{{docker tag}} {{container_name:latest}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name:latest}}`

- Push an image to a repository:

`{{docker push}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name:latest}}`

- Pull an image from a repository:

`{{docker pull}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name:latest}}`

- Delete an image from a repository:

`aws ecr batch-delete-image  --repository-name {{repo_name}} --image-ids imageTag={{latest}}`

- Delete a repository:

`aws ecr delete-repository --repository-name {{repo_name}} --force`

- List images in a repository:

`aws ecr list-images --repository-name {{repo_name}}`
