# export

> 셸 변수를 하위 프로세스로 내보냅니다.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-export>.

- 환경 변수를 설정:

`export {{변수}}={{값}}`

- 환경 변수를 해제:

`export -n {{변수}}`

- 함수를 하위 프로세스로 내보내기:

`export -f {{함수_이름}}`

- 환경 변수 `PATH`에 경로명 추가:

`export PATH=$PATH:{{경로/대상/추가}}`

- 셸 명령 형태로 활성화된 내보낸 변수 목록 표시:

`export -p`
