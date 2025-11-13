# tmpmail

> 터미널에서 바로 사용할 수 있는 POSIX sh로 작성된 임시 이메일.
> 더 많은 정보: <https://github.com/sdushantha/tmpmail#usage>.

- 임시 받은 편지함 생성:

`tmpmail --generate`

- 메시지와 그 숫자 ID 나열:

`tmpmail`

- 가장 최근에 받은 이메일 표시:

`tmpmail --recent`

- 특정 메시지 열기:

`tmpmail {{이메일_ID}}`

- HTML 태그 없이 이메일을 원시 텍스트로 보기:

`tmpmail --text`

- 특정 브라우저로 이메일 열기 (기본값은 w3m):

`tmpmail --browser {{브라우저}}`
