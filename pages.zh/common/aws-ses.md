# aws ses

> AWS简单电子邮件服务的命令行工具。
> 高规模的入站和出站云电子邮件服务。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>。

- 创建一个新的接收规则集：

`aws ses create-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- 描述当前活动的接收规则集：

`aws ses describe-active-receipt-rule-set --generate-cli-skeleton`

- 描述一个特定的接收规则：

`aws ses describe-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- 列出所有接收规则集：

`aws ses list-receipt-rule-sets --starting-token {{token_string}} --max-items {{integer}} --generate-cli-skeleton`

- 删除一个特定的接收规则集（当前活动的规则集不能被删除）：

`aws ses delete-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- 删除一个特定的接收规则：

`aws ses delete-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- 发送电子邮件：

`aws ses send-email --from {{from_address}} --destination "ToAddresses={{addresses}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}"`

- 显示特定SES子命令的帮助：

`aws ses {{subcommand}} help`