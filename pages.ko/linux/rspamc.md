# rspamc

> rspamd 서버용 커맨드라인 클라이언트.
> 더 많은 정보: <https://manned.org/rspamc>.

- 베이지안 필터를 훈련시켜 이메일을 스팸으로 인식:

`rspamc learn_spam {{경로/대상/이메일_파일}}`

- 베이지안 필터를 훈련시켜 이메일을 정상 메일로 인식:

`rspamc learn_ham {{경로/대상/이메일_파일}}`

- 이메일에 대한 수동 보고서 생성:

`rspamc symbols {{경로/대상/이메일_파일}}`

- 서버 통계 표시:

`rspamc stat`
