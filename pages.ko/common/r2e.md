# r2e

> RSS 피드를 이메일 주소로 전달.
> 설정된 `sendmail` 또는 SMTP 설정이 필요합니다.
> 더 많은 정보: <https://github.com/rss2email/rss2email>.

- 이메일 주소로 이메일을 보내는 새로운 피드 데이터베이스 생성:

`r2e new {{이메일_주소}}`

- 피드 구독:

`r2e add {{피드_이름}} {{피드_URI}}`

- 새로운 이야기를 이메일 주소로 전송:

`r2e run`

- 모든 피드 나열:

`r2e list`

- 지정된 색인의 피드 삭제:

`r2e delete {{색인}}`
