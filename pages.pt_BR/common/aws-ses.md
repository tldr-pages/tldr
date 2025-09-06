# aws ses

> Interface de linha de comando para o AWS Simple Email Service.
> Serviço em nuvem com alta performance para envio e recebimento de emails.
> Mais informações: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- Cria um novo conjunto de regras:

`aws ses create-receipt-rule-set --rule-set-name {{nome_do_conjunto_de_regras}} --generate-cli-skeleton`

- Descreve os conjuntos ativos de regras:

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- Descreve um regra específica de um conjunto de regras:

`aws ses describe-receipt-rule --rule-set-name {{nome_do_conjunto_de_regras}} --rule-name {{nome_da_regra}} --generate-cli-skeleton`

- Lista todos os conjuntos de regras:

`aws ses list-receipt-rule-sets --starting-token {{texto_do_token}} --max-items {{inteiro}} --generate-cli-skeleton`

- Remove um conjunto de regras específico (o conjunto ativo não pode ser removido):

`aws ses delete-receipt-rule-set --rule-set-name {{nome_do_conjunto_de_regras}} --generate-cli-skeleton`

- Remove uma regras específica de um conjunto de regras:

`aws ses delete-receipt-rule --rule-set-name {{nome_do_conjunto_de_regras}} --rule-name {{nome_da_regra}} --generate-cli-skeleton`

- Envia um email:

`aws ses send-email --from {{de_endereco}} --destination "ToAddresses={{para_endereco}}" --message "Subject={Data={{assunto}},Charset=utf8},Body={Text={Data={{corpo_email}},Charset=utf8},Html={Data={{corpo_do_email_com_html}},Charset=utf8}}"`

- Exibe ajuda para um subcomando específico do SES:

`aws ses {{subcomando}} help`
