# aws configure

> Gerencia as configurações para o AWS CLI.
> Mais informações: <https://docs.aws.amazon.com/cli/latest/reference/configure/>.

- Configura interativamente o AWS CLI (cria uma nova configuração ou atualiza a configuração default):

`aws configure`

- Configura interativamente um profile para o AWS CLI (cria um novo profile ou atualiza um que já existae):

`aws configure --profile {{nome_do_profile}}`

- Exibe o valor de uma variável específica de configuração:

`aws configure get {{nome}}`

- Exibe o valor de uma variável específica de configuração de um profile específico:

`aws configure get {{nome}} --profile {{nome_do_profile}}`

- Altera o valor de uma variável específica de configuração:

`aws configure set {{nome}} {{valor}}`

- Altera o valor de uma variável específica de configuração de um profile específico:

`aws configure set {{nome}} {{valor}} --profile {{nome_do_profile}}`

- Lista os entradas da configuração:

`aws configure list`

- Lista os entradas da configuração de um profile específico:

`aws configure list --profile {{profile_name}}`
