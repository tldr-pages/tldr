# git magic

> 추가, 커밋 및 푸시 루틴 자동화.
> `git-extras`의 일부.
> 더 많은 정보: <https://manned.org/git-magic>.

- 생성된 메시지로 변경 사항 커밋:

`git magic`

- 추적되지 않은 파일을 [a]dd하고 생성된 메시지로 변경 사항 커밋:

`git magic -a`

- 사용자 정의 [m]essage로 변경 사항 커밋:

`git magic -m "{{사용자_커밋_메시지}}"`

- 커밋하기 전에 커밋 [m]essage를 [e]dit:

`git magic -em "{{사용자_커밋_메시지}}"`

- 변경 사항 커밋 및 원격 저장소에 [p]ush:

`git magic -p`

- 변경 사항 커밋 및 원격 저장소에 [f]orce [p]ush:

`git magic -fp`
