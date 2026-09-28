# wacli send file

> WhatsApp을 통해 파일을 전송 (이미지, 비디오, 오디오 또는 문서).
> 관련 항목: `wacli send text`.
> 더 많은 정보: <https://wacli.sh/send.html>.

- 전화번호로 파일을 전송:

`wacli send file --to {{전화번호}} --file {{경로/대상/파일}}`

- 지정한 JID로 파일 전송:

`wacli send file --to {{전화번호}}@s.whatsapp.net --file {{경로/대상/파일}}`

- 사용자 지정 타임아웃을 설정하여 파일 전송:

`wacli send file --to {{전화번호}} --file {{경로/대상/파일}} --timeout {{10m}}`
