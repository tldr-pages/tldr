# doas

> 다른 사용자로 명령을 실행.
> 더 많은 정보: <https://man.openbsd.org/doas>.

- 루트 권한으로 명령을 실행:

`doas {{명령어}}`

- 다른 사용자 권한으로 명령을 실행:

`doas -u {{사용자}} {{명령어}}`

- 루트 권한으로 기본 쉘을 시작:

`doas -s`

- 구성 파일을 구문 분석하고, 다른 사용자로 명령 실행이 허용되는지 확인:

`doas -C {{구성_파일}} {{명령어}}`

- `doas`가 이전에 제공된 후에도 비밀번호를 요청하도록 함:

`doas -L`