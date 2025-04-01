# aws ses

> AWS 简单邮件服务 (SES) 的命令行接口。
> 提供大规模的云端邮件发送和接收服务。
> 更多信息：<https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- 创建新的接收规则集：

`aws ses create-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- 描述当前活动的接收规则集：

`aws ses describe-active-receipt-rule-set --generate-cli-skeleton`

- 描述特定的接收规则：

`aws ses describe-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- 列出所有的接收规则集：

`aws ses list-receipt-rule-sets --starting-token {{token_string}} --max-items {{integer}} --generate-cli-skeleton`

- 删除特定的接收规则集（当前活动的规则集不能被删除）：

`aws ses delete-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- 删除特定的接收规则：

`aws ses delete-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- 发送邮件：

`aws ses send-email --from {{from_address}} --destination "ToAddresses={{addresses}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}}"`

- 显示特定 SES 子命令的帮助信息：

`aws ses {{subcommand}} help`