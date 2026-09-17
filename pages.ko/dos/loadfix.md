# LOADFIX

> 구형 프로그램 실행을 위한 사용 가능한 기본 메모리를 줄이는 명령어 (기본: 64KB).
> 더 많은 정보: <https://www.dosbox.com/wiki/LOADFIX>.

- 64KB 할당된 메모리로 프로그램 시작:

`LOADFIX {{프로그램}}`

- 사용자 정의 KB만큼 메모리 줄이기 (1-1024):

`LOADFIX -{{32}} {{프로그램}}`

- 이전 할당된 메모리 모두 해제:

`LOADFIX -f`
