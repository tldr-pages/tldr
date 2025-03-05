# top

> 실행 중인 프로세스에 대한 동적 실시간 정보 표시.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/top.1.html>.

- `top` 시작, 모든 옵션은 인터페이스에서 사용 가능:

`top`

- 내부 메모리 크기로 프로세스를 정렬하여 `top` 시작 (기본 순서 - 프로세스 ID):

`top -o mem`

- CPU 사용량, 실행 시간 순으로 프로세스를 정렬하여 `top` 시작:

`top -o cpu -O time`

- 지정된 사용자가 소유한 프로세스만 표시하여 `top` 시작:

`top -user {{사용자_이름}}`

- 대화형 명령에 대한 도움말 표시:

`<?>`
