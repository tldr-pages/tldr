# aws ses

> AWS Simple Email Service 的 CLI。
> 高可扩展的云端入站和出站电子邮件服务。
> 更多信息：<https://docs.aws.amazon.com/cli/latest/reference/ses/>.

- 创建一个新的接收规则集：

`aws ses create-receipt-rule-set --rule-set-name {{规则集名称}} --generate-cli-skeleton`

- 描述当前处于活动状态的接收规则集：

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- 描述一个特定的接收规则：

`aws ses describe-receipt-rule --rule-set-name {{规则集名称}} --rule-name {{规则名称}} --generate-cli-skeleton`

- 列出所有接收规则集：

`aws ses list-receipt-rule-sets --starting-token {{令牌字符串}} --max-items {{整数}} --generate-cli-skeleton`

- 删除一个特定的接收规则集（当前处于活动状态的规则集无法被删除）：

`aws ses delete-receipt-rule-set --rule-set-name {{规则集名称}} --generate-cli-skeleton`

- 删除一个特定的接收规则：

`aws ses delete-receipt-rule --rule-set-name {{规则集名称}} --rule-name {{规则名称}} --generate-cli-skeleton`

- 发送一封电子邮件：

`aws ses send-email --from {{发件人地址}} --destination "ToAddresses={{收件人地址列表}}" --message "Subject={Data={{主题文本}},Charset=utf8},Body={Text={Data={{正文文本}},Charset=utf8},Html={Data={{包含 HTML 的邮件正文}},Charset=utf8}}"`

- 显示特定 SES 子命令的帮助信息：

`aws ses {{子命令}} help`
