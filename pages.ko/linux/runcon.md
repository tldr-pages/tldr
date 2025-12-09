# runcon

> 프로그램을 다른 SELinux 보안 컨텍스트에서 실행.
> 같이 보기: `secon`.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/runcon-invocation.html>.

- 현재 실행 컨텍스트의 보안 컨텍스트를 출력:

`runcon`

- 명령을 실행할 도메인 지정:

`runcon {{[-t|--type]}} {{도메인}}_t {{명령어}}`

- 명령을 실행할 컨텍스트 역할 지정:

`runcon {{[-r|--role]}} {{역할}}_r {{명령어}}`

- 명령을 실행할 전체 컨텍스트 지정:

`runcon {{사용자}}_u:{{역할}}_r:{{도메인}}_t {{명령어}}`
