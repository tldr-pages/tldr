# dolt config

> 로컬(저장소별) 및 글로벌(사용자별) Dolt 구성 변수를 읽고 씁니다.
> 더 많은 정보: <https://docs.dolthub.com/cli-reference/cli#dolt-config>.

- 모든 로컬 및 글로벌 구성 옵션과 그 값을 나열:

`dolt config --list`

- 로컬 또는 글로벌 구성 변수의 값을 표시:

`dolt config --get {{이름}}`

- 로컬 구성 변수의 값을 수정하고, 존재하지 않으면 생성:

`dolt config --add {{이름}} {{값}}`

- 글로벌 구성 변수의 값을 수정하고, 존재하지 않으면 생성:

`dolt config --global --add {{이름}} {{값}}`

- 로컬 구성 변수를 삭제:

`dolt config --unset {{이름}}`

- 글로벌 구성 변수를 삭제:

`dolt config --global --unset {{이름}}`
