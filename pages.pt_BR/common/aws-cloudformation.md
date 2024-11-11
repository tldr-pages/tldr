# aws cloudformation

> Modela, provisiona e gerencia recursos AWS, e de terceiros, ao tratar a infraestrutura como código.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/cloudformation/index.html>.

- Cria uma pilha a partir de um arquivo de modelo:

`aws cloudformation create-stack --stack-name {{nome-da-pilha}} --region {{região}} --template-body {{file://caminho/para/arquivo.yml}} --profile {{perfil}}`

- Deleta uma pilha:

`aws cloudformation delete-stack --stack-name {{nome-da-pilha}} --profile {{perfil}}`

- Lista todas as pilhas:

`aws cloudformation list-stacks --profile {{perfil}}`

- Lista todas as pilhas em execução:

`aws cloudformation list-stacks --stack-status-filter CREATE_COMPLETE --profile {{perfil}}`

- Verifica o status de uma pilha:

`aws cloudformation describe-stacks --stack-name {{id-da-pilha}} --profile {{perfil}}`

- Inicia a detecção de desvio para uma pilha:

`aws cloudformation detect-stack-drift --stack-name {{id-da-pilha}} --profile {{perfil}}`

- Verifica o status de desvio de uma pilha usando 'StackDriftDetectionId' do resultado do comando anterior:

`aws cloudformation describe-stack-resource-drifts --stack-name {{stack-drift-detection-id}} --profile {{perfil}}`
