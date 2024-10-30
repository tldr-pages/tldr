# dolt commit

> 테이블에 대한 단계적인 변경 사항을 커밋.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-commit>.

- 커밋 메시지를 입력하려면 `$EDITOR`로 지정된 편집기를 열어 모든 단계적 변경 사항을 커밋:

`dolt commit`

- 지정된 메시지로 모든 단계적 변경 사항을 커밋:

`dolt commit --message "{{커밋_메시지}}"`

- 커밋하기 전에, 테이블에 대한 모든 스테이지되지 않은 변경 사항을 스테이징함:

`dolt commit --all`

- 지정된 ISO 8601 커밋 날짜를 사용 (기본값은 현재 날짜 및 시간):

`dolt commit --date "{{2021-12-31T00:00:00}}"`

- 커밋에 지정된 작성자를 사용:

`dolt commit --author "{{작성자_이름}} <{{작성자_이메일}}>"`

- 변경 사항 없이, 빈 커밋 생성을 허용:

`dolt commit --allow-empty`

- 외래 키 경고를 무시:

`dolt commit --force`
