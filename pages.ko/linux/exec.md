# exec

> 자식 프로세스를 생성하지 않고 명령을 실행합니다.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-exec>.

- 특정 명령 실행:

`exec {{명령어 -옵션 -플래그}}`

- (거의) 빈 환경에서 명령 실행:

`exec -c {{명령어 -옵션 -플래그}}`

- 로그인 셸로 명령 실행:

`exec -l {{명령어 -옵션 -플래그}}`

- 다른 이름으로 명령 실행:

`exec -a {{이름}} {{명령어 -옵션 -플래그}}`
