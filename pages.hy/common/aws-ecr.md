# aws ecr

> Հրել, քաշել և կառավարել կոնտեյների պատկերները:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/ecr/>:.

- Նույնականացրեք Docker-ը լռելյայն ռեգիստրով (օգտանունը AWS է).:

`aws ecr get-login-password --region {{region}} | {{docker login}} --username AWS --password-stdin {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com`

- Ստեղծեք պահեստ.:

`aws ecr create-repository --repository-name {{repository}} --image-scanning-configuration scanOnPush={{true|false}} --region {{region}}`

- Նշեք տեղական պատկեր ECR-ի համար.:

`docker tag {{container_name}}:{{tag}} {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Պատկերը տեղափոխեք պահեստ.:

`docker push {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Քաշեք պատկերը պահոցից.:

`docker pull {{aws_account_id}}.dkr.ecr.{{region}}.amazonaws.com/{{container_name}}:{{tag}}`

- Ջնջել պատկերը պահեստից.:

`aws ecr batch-delete-image --repository-name {{repository}} --image-ids imageTag={{latest}}`

- Ջնջել պահեստը.:

`aws ecr delete-repository --repository-name {{repository}} --force`

- Թվարկեք պատկերները պահեստում.:

`aws ecr list-images --repository-name {{repository}}`
