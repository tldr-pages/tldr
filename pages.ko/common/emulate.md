# emulate

> 특정 쉘의 동작을 모방하도록 쉘 옵션 재설정.
> 쉘 함수가 기본 설정으로 실행되도록 보장하는 데에도 사용됨.
> 더 많은 정보: <https://github.com/antonio/zsh-config/blob/master/help/emulate>.

- 현재 에뮬레이션 모드 출력:

`emulate`

- 현재 쉘 세션 설정을 Bash처럼 동작하도록 조정:

`emulate bash`

- 임시 에뮬레이션 환경에서 명령([c]ommand) 실행:

`emulate ksh -c "{{echo hi}}"`

- 기본 Zsh 환경을 에뮬레이션하고 가능하면 옵션 재설정([R]esetting):

`emulate zsh -R`

- 현재 함수 범위 내에서만 에뮬레이션 적용:

`{{my_function}}() { emulate -L {{zsh|sh|ksh|csh}}; {{ls}} }`
