# wacli messages list

> WhatsApp 채팅 메시지 목록을 표시.
> 관련 항목: `wacli messages search`, `wacli messages show`, `wacli messages context`.
> 더 많은 정보: <https://wacli.sh/messages.html>.

- 지정한 채팅의 메시지 목록을 JSON 형식으로 표시:

`wacli messages list --chat {{전화번호}}@s.whatsapp.net --json`

- 지정한 날짜 이후에 수신된 메시지 목록 표시:

`wacli messages list --chat {{전화번호}}@s.whatsapp.net --after {{2026-01-28}} --json`

- 지정한 날짜 이전에 수신된 메시지 목록 표시:

`wacli messages list --chat {{전화번호}}@s.whatsapp.net --before {{2026-01-28}} --json`

- 지정한 날짜 범위에 수신된 메시지 목록 표시:

`wacli messages list --chat {{전화번호}}@s.whatsapp.net --after {{2026-01-01}} --before {{2026-01-31}} --json`

- 표시할 결과 개수 제한:

`wacli messages list --chat {{전화번호}}@s.whatsapp.net --limit {{10}} --json`
