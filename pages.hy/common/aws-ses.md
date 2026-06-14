# ws ses

> CLI AWS էլփոստի պարզ ծառայության համար:.
> Բարձր մասշտաբի ներգնա և ելքային ամպային էլփոստի ծառայություն:.
> Լրացուցիչ տեղեկություններ. <https://docs.aws.amazon.com/cli/latest/reference/ses/>:.

- Ստեղծեք նոր անդորրագրի կանոնների հավաքածու.:

`aws ses create-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- Նկարագրեք ակտիվ ստացման կանոնների հավաքածուն.:

`aws ses describe-active-receipt-rule-set --generate-cli-skeleton`

- Նկարագրեք ստացման հատուկ կանոն.:

`aws ses describe-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- Թվարկեք բոլոր ստացման կանոնների հավաքածուները.:

`aws ses list-receipt-rule-sets --starting-token {{token_string}} --max-items {{integer}} --generate-cli-skeleton`

- Ջնջել անդորրագրի կանոնների հատուկ հավաքածու (ներկայիս գործող կանոնների հավաքածուն չի կարող ջնջվել).:

`aws ses delete-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- Ջնջել անդորրագրի հատուկ կանոնը.:

`aws ses delete-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- Ուղարկել էլ.:

`aws ses send-email --from {{from_address}} --destination "ToAddresses={{addresses}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}}"`

- Ցուցադրել օգնություն հատուկ SES ենթահրամանի համար.:

`aws ses {{subcommand}} help`
