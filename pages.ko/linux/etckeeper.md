# etckeeper

> 시스템 구성 파일을 Git으로 추적합니다.
> 더 많은 정보: <https://manned.org/etckeeper>.

- Git 저장소를 설정하고 다양한 설정 작업 수행(`/etc`에서 실행):

`sudo etckeeper init`

- `/etc`의 모든 변경 사항 커밋:

`sudo etckeeper commit {{메시지}}`

- 임의의 Git 명령 실행:

`sudo etckeeper vcs {{status}}`

- 커밋되지 않은 변경 사항이 있는지 확인(종료 코드만 반환):

`sudo etckeeper unclean`

- 기존 저장소를 삭제하고 변경 사항 추적 중지:

`sudo etckeeper uninit`
