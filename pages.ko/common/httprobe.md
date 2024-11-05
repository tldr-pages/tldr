# httprobe

> 작동하는 HTTP 및 HTTPS 서버에 대한 도메인 밒 프로브 목록을 가져옴.
> 더 많은 정보: <https://github.com/tomnomnom/httprobe>.

- 텍스트 파일에서 도에인 목록을 조사:

`cat {{입력_파일}} | httprobe`

- HTTPS가 작동하지 않는 경우에만 HTTP 확인:

`cat {{입력_파일}} | httprobe --prefer-https`

- 특정 프로토콜을 사용하여 추가 포트를 조사:

`cat {{입력_파일}} | httprobe -p {{https:2222}}`

- 도움말 표시:

`httprobe --help`
