# mutt

> 커맨드라인 이메일 클라이언트.
> 더 많은 정보: <http://mutt.org/doc/mutt.1.txt>.

- 지정된 메일박스 열기:

`mutt -f {{메일박스}}`

- 이메일을 보내며 제목과 참조 수신자를 지정:

`mutt -s {{제목}} -c {{참조@example.com}} {{수신자@example.com}}`

- 파일을 첨부하여 이메일 보내기:

`mutt -a {{파일1}} {{파일2}} -- {{수신자@example.com}}`

- 메시지 본문으로 포함할 파일 지정:

`mutt -i {{경로/대상/파일}} {{수신자@example.com}}`

- RFC 5322 형식으로 헤더와 본문을 포함한 초안 파일 지정:

`mutt -H {{경로/대상/파일}} {{수신자@example.com}}`
