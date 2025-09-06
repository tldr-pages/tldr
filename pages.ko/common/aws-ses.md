# aws ses

> AWS Simple Email Service용 CLI.
> 대규모 인바운드 및 아운바운드 클라우드 이메일 서비스.
> 더 많은 정보: <https://awscli.amazonaws.com/v2/documentation/api/latest/reference/ses/index.html>.

- 새로운 수신 규칙 세트를 생성:

`aws ses create-receipt-rule-set --rule-set-name {{정책_모음_이름}} --generate-cli-skeleton`

- 활성 수신 규칙 세트 정보를 표시:

`aws ses describe-active-receipt-rule-set --generate-cli-skeletion`

- 특정 수신 규칙 정보를 표시:

`aws ses describe-receipt-rule --rule-set-name {{정책_모음_이름}} --rule-name {{정책_이름}} --generate-cli-skeleton`

- 모든 수신 규칙 세트를 나열:

`aws ses list-receipt-rule-sets --starting-token {{토큰_문자열}} --max-items {{정수}} --generate-cli-skeleton`

- 특정 수신 규칙 세트 삭제 (현재 활성화된 규칙 세트는 삭제할 수 없음):

`aws ses delete-receipt-rule-set --rule-set-name {{규칙_정보_이름}} --generate-cli-skeleton`

- 특정 수신 규칙 삭제:

`aws ses delete-receipt-rule --rule-set-name {{규칙_정보_이름}} --rule-name {{규칙_이름}} --generate-cli-skeleton`

- 이메일 전송:

`aws ses send-email --from {{송신_주소}} --destination "ToAddresses={{주소}}" --message "Subject={Data={{subject_text}},Charset=utf8},Body={Text={Data={{body_text}},Charset=utf8},Html={Data={{message_body_containing_html}},Charset=utf8}}"`

- 특정 SES 하위 명령어에 대한 도움말 표시:

`aws ses {{하위명령어}} help`
