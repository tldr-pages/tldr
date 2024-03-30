# aws sts

> Serviço de Token de Segurança (STS) que permite solicitar credenciais temporárias para usuários (IAM) ou federados.
> Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/sts/>.

- Obtém credenciais temporárias para acessar recursos AWS específicos:

`aws sts assume-role --role-arn {{arn_do_papel_aws}}`

- Obtém um usuário IAM ou papel que foi usado para chamar a operação:

`aws sts get-caller-identity`
