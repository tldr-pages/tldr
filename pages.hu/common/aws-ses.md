# aws ses

> CLI az AWS Simple Email Service-hez. Nagyszabású bejövő és kimenő felhőalapú e-mail szolgáltatás. További információ: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- Hozzon létre egy új átvételi szabálykészletet:

`aws ses create-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- Írja le az aktív átvételi szabálykészletet:

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- Egy adott átvételi szabály leírása:

`aws ses describe-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- Az összes átvételi szabálykészlet listázása:

`aws ses list-receipt-rule-sets --starting-token {{token_string}} --max-items {{integer}} --generate-cli-skeleton`

- Egy adott vételi szabálykészlet törlése (a jelenleg aktív szabálykészlet nem törölhető):

`aws ses delete-receipt-rule-set --rule-set-name {{rule_set_name}} --generate-cli-skeleton`

- Egy adott nyugtázási szabály törlése:

`aws ses delete-receipt-rule --rule-set-name {{rule_set_name}} --rule-name {{rule_name}} --generate-cli-skeleton`

- E-mail küldése:

`aws ses send-email --from {{from_address}} --destination "ToAddresses={{addresses}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}}"`

- Egy adott SES-alparancshoz tartozó súgó megjelenítése:

`aws ses {{subcommand}} help`
