# mail

> 사용자 메일박스 조회 및 메일 송수신.
> 메일 본문은 `stdin`을 통해 입력됨.
> 더 많은 정보: <https://manned.org/mail>.

- 개인 메일을 확인하기 위한 대화형 프롬프트 열기:

`mail`

- 입력한 이메일 메시지를 선택적으로 참조(CC)와 함께 보내기. 아래 명령은 `<Enter>`를 누른 후 계속됩니다. 메시지 텍스트를 입력하세요(여러 줄 가능). 메시지 입력이 완료되면 `<Ctrl d>`를 누르세요:

`mail --subject "{{제목}}" {{받는사람@example.com}} --cc "{{참조_이메일_주소}}"`

- 파일 내용을 포함하는 이메일 보내기:

`mail < {{경로/대상/파일.txt}} --subject "{{$HOSTNAME 파일명.txt}}" {{받는사람@example.com}}`

- `.tar.gz` 파일을 첨부 파일로 보내기:

`tar cvzf - {{경로/대상/디렉터리1 경로/대상/디렉터리2}} | uuencode {{데이터.tar.gz}} | mail --subject "{{제목}}" {{받는사람@example.com}}`

- 도움말 표시:

`mail {{[-h|--help]}}`
