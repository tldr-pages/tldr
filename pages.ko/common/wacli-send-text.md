# wacli send text

> WhatsApp을 통해 텍스트 메시지를 전송.
> 관련 항목: `wacli send file`.
> 더 많은 정보: <https://wacli.sh/send.html>.

- 전화번호로 텍스트 메시지 전송:

`wacli send text --to {{전화번호}} --message "{{메시지}}"`

- 지정한 JID로 텍스트 메시지 전송:

`wacli send text --to {{전화번호}}@s.whatsapp.net --message "{{메시지}}"`

- 사용자 지정 타임아웃을 설정해 텍스트 메시지 전송:

`wacli send text --to {{전화번호}} --message "{{메시지}}" --timeout {{10m}}`

- 사용자 지정 저장소 경로를 사용하여 텍스트 메시지 전송:

`wacli send text --to {{전화번호}} --message "{{메시지}}" --store {{경로/대상/저장소}}`
