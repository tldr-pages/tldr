# aws

> A interface de linha de comando oficial para o Amazon Web Services.
> Passo-a-passo, Single Sign-On (SSO), autocompletar de recursos e opções de YAML somente na v2.
> Alguns subcomandos como `aws s3` tem sua própia documentação de uso.
> Mais informações: <https://aws.amazon.com/cli>.

- Configura a linha de comando da AWS:

`aws configure wizard`

- Configura a linha de comando da AWS usando o SSO:

`aws configure sso`

- Veja o texto de ajuda para o comando da AWS:

`aws {{comando}} help`

- Obtenha a informações da identidade usada (útil para analisar problemas de permissão):

`aws sts get-caller-identity`

- Lista recursos da AWS em uma região em yaml:

`aws dynamodb list-tables --region {{sa-east-1}} --output yaml`

- Usa prompt de comando para ajuda com o preenchimento:

`aws iam create-user --cli-auto-prompt`

- Usa um passo-a-passo interativo para um recurso da AWS:

`aws dynamodb wizard {{nova-tabela}}`

- Gera um arquivo esqueleo em JSON (útil para ser usado em infraestrutura como código):

`aws dynamodb update-table --generate-cli-skeleton`
