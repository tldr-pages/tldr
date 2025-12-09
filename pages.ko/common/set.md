# set

> 셸 옵션을 토글하거나 위치 매개변수의 값을 설정.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#The-Set-Builtin>.

- 셸 변수의 이름과 값을 표시:

`set`

- 새로 초기화된 변수를 자식 프로세스에 내보내기:

`set -a`

- 작업이 완료될 때 `stderr`에 형식화된 메시지 쓰기:

`set -b`

- `vi`와 유사한 키 바인딩(e.g. `yy`)으로 명령줄에서 텍스트 쓰기 및 편집:

`set -o {{vi}}`

- 기본 모드로 돌아가기:

`set -o {{emacs}}`

- 모든 모드 나열:

`set -o`

- (일부) 명령이 실패할 때 셸 종료:

`set -e`
