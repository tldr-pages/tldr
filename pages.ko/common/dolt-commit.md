# dolt commit

> 스테이징된 변경 사항을 테이블에 커밋.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-commit>.

- 모든 스테이징된 변경 사항을 커밋하고, `$EDITOR`에 지정된 편집기를 열어 커밋 메시지 입력:

`dolt commit`

- 지정된 메시지로 모든 스테이징된 변경 사항 커밋:

`dolt commit --message "{{커밋_메시지}}"`

- 커밋 전에 모든 스테이징되지 않은 테이블 변경 사항 스테이징:

`dolt commit --all`

- 지정된 ISO 8601 커밋 날짜 사용 (기본값은 현재 날짜와 시간):

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- 지정된 작성자를 사용하여 커밋:

`dolt commit --author "{{작성자_이름}} <{{작성자_이메일}}>"`

- 변경 사항 없이 빈 커밋 생성 허용:

`dolt commit --allow-empty`

- 외래 키 경고 무시:

`dolt commit --force`
