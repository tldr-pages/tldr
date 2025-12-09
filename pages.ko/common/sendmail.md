# sendmail

> 이메일 보내기.
> 더 많은 정보: <https://manned.org/sendmail>.

- `message.txt`의 내용을 로컬 사용자 `username`의 메일 디렉토리로 전송:

`sendmail {{username}} < {{message.txt}}`

- 메일 서버가 설정되어 있다고 가정하고, you@yourdomain.com에서 test@gmail.com으로 `message.txt`의 내용을 포함한 이메일 보내기:

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{message.txt}}`

- 메일 서버가 설정되어 있다고 가정하고, you@yourdomain.com에서 test@gmail.com으로 `file.zip` 파일을 포함한 이메일 보내기:

`sendmail -f {{you@yourdomain.com}} {{test@gmail.com}} < {{file.zip}}`
