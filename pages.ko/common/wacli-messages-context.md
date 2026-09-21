# wacli messages context

> 특정 WhatsApp 메시지의 앞 뒤에 있는 메시지를 표시.
> 관련 항목: `wacli messages show`, `wacli messages list`.
> 더 많은 정보: <https://wacli.sh/messages.html>.

- 지정한 메시지 주변의 대화 내용을 JSON 형식으로 표시:

`wacli messages context {{메시지_아이디}} --json`

- 사용자 지정 저장소를 사용해 지정한 메시지 주변의 대화 내용으로 표시:

`wacli messages context {{메시지_아이디}} --json --store {{경로/대상/저장소}}`
