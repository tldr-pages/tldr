# leaks

> 프로세스 메모리에서 참조되지 않는 malloc 버퍼를 검색.
> 더 많은 정보: <https://keith.github.io/xcode-man-pages/leaks.1.html>.

- 이름을 지정하여 실행 중인 프로세스의 메모리 누수 검사:

`leaks {{프로세스_이름}}`

- PID를 지정하여 실행 중인 프로세스의 메모리 누수 검사:

`leaks {{프로세스_아이디}}`

- 명령을 실행하고 종료 시 메모리 누수 검사:

`leaks -atExit -- {{명령어}}`

- `MallocStackLogging` 환경 변수를 설정해 각 메모리 누수의 백트레이스 활성화:

`MallocStackLogging=YES leaks {{프로세스_이름}}`

- 트리 대신 기존 목록 형식으로 결과 표시:

`leaks -list {{프로세스_이름}}`

- 누수된 객체를 유형별로 그룹화:

`leaks -groupByType {{프로세스_이름}}`

- 나중에 분석할 수 있도록 메모리 상태를 메모리 그래프 파일로 저장:

`leaks {{프로세스_이름}} -outputGraph {{경로/대상/파일.memgraph}}`

- 이전에 저장한 메모리 그래프 파일 검사:

`leaks {{경로/대상/파일.memgraph}}`
