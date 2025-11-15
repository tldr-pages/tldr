# neomutt

> NeoMutt 명령줄 이메일 클라이언트.
> 더 많은 정보: <https://neomutt.org/guide/reference.html>.

- 지정된 메일박스 열기:

`neomutt -f {{경로/대상/메일박스}}`

- 이메일 작성 시작 및 제목과 `cc` 수신자 지정:

`neomutt -s "{{제목}}" -c {{cc@example.com}} {{recipient@example.com}}`

- 첨부 파일과 함께 이메일 보내기:

`neomutt -a {{경로/대상/파일1 경로/대상/파일2 ...}} -- {{recipient@example.com}}`

- 메시지 본문으로 포함할 파일 지정:

`neomutt -i {{경로/대상/파일}} {{recipient@example.com}}`

- RFC 5322 형식의 헤더와 본문이 포함된 초안 파일 지정:

`neomutt -H {{경로/대상/파일}} {{recipient@example.com}}`
