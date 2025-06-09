# chcon

> 파일 또는 파일/디렉토리의 SELinux 보안 컨텍스트를 변경합니다.
> 같이 보기: `secon`, `restorecon`, `semanage-fcontext`.
> 더 많은 정보: <https://www.gnu.org/software/coreutils/manual/html_node/chcon-invocation.html>.

- 파일의 보안 컨텍스트 보기:

`ls {{[-lZ|-l --context]}} {{경로/대상/파일}}`

- 참조된 파일을 사용하여, 대상 파일의 보안 내용 변경:

`chcon --reference {{참조_파일}} {{대상_파일}}`

- 파일의 전체 SELinux 보안 컨텍스트 변경:

`chcon {{사용자}}:{{역할}}:{{타입}}:{{범위/레벨}} {{파일명}}`

- SELinux 보안 컨텍스트의 사용자 부분만 변경:

`chcon {{[-u|--user]}} {{사용자}} {{파일명}}`

- SELinux 보안 컨텍스트의 역할 부분만 변경:

`chcon {{[-r|--role]}} {{역할}} {{파일명}}`

- SELinux 보안 컨텍스트의 유형 부분만 변경:

`chcon {{[-t|--type]}} {{타입}} {{파일명}}`

- SELinux 보안 컨텍스트의 범위/레벨 부분만 변경:

`chcon {{[-l|--range]}} {{범위/레벨}} {{파일명}}`
