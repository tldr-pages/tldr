# trap

> 이벤트 발생 시 명령을 실행합니다.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-trap>.

- 사용 가능한 이벤트 이름 나열 (예: `SIGWINCH`):

`trap -l`

- 명령과 예상 이벤트 이름 나열:

`trap -p`

- 신호를 받았을 때 명령 실행:

`trap 'echo "Caught signal {{SIGHUP}}"' {{SIGHUP}}`

- 명령 제거:

`trap - {{SIGHUP}} {{SIGINT}}`
