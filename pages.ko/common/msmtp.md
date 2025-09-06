# msmtp

> SMTP 클라이언트.
> `stdin`에서 텍스트를 읽고 이를 SMTP 서버로 전송합니다.
> 더 많은 정보: <https://marlam.de/msmtp>.

- `~/.msmtprc`에 설정된 기본 계정을 사용하여 이메일 전송:

`echo "{{안녕하세요}}" | msmtp {{to@example.org}}`

- `~/.msmtprc`에 설정된 특정 계정을 사용하여 이메일 전송:

`echo "{{안녕하세요}}" | msmtp --account={{계정_이름}} {{to@example.org}}`

- 설정된 계정 없이 이메일 전송. 비밀번호는 `~/.msmtprc` 파일에 명시해야 합니다:

`echo "{{안녕하세요}}" | msmtp --host={{localhost}} --port={{999}} --from={{from@example.org}} {{to@example.org}}`
