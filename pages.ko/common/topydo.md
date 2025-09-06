# topydo

> todo.txt 형식을 사용하는 할 일 목록 애플리케이션.
> 더 많은 정보: <https://github.com/topydo/topydo>.

- 특정 프로젝트와 주어진 컨텍스트로 할 일 추가:

`topydo add "{{할일_메시지}} +{{프로젝트_이름}} @{{컨텍스트_이름}}"`

- 마감일이 내일이고 우선순위가 `A`인 할 일 추가:

`topydo add "(A) {{할일_메시지}} due:{{1d}}"`

- 마감일이 금요일인 할 일 추가:

`topydo add "{{할일_메시지}} due:{{fri}}"`

- 비엄격한 반복 할 일 추가 (다음 마감일 = 지금 + 반복):

`topydo add "물 주기 due:{{mon}} rec:{{1w}}"`

- 엄격한 반복 할 일 추가 (다음 마감일 = 현재 마감일 + 반복):

`topydo add "{{할일_메시지}} due:{{2020-01-01}} rec:{{+1m}}"`

- 마지막으로 실행한 `topydo` 명령 되돌리기:

`topydo revert`
