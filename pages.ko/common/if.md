# if

> 쉘 스크립트에서 조건부 처리를 수행.
> 참고: `test`, `[`.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#Conditional-Constructs>.

- 조건 명령어의 종료 상태가 0인 경우, 지정된 명령을 실행:

`if {{조건_명령어}}; then {{echo "Condition is true"}}; fi`

- 조건 명령어의 종료 상태가 0이 아닌 경우, 지정된 명령을 실행:

`if ! {{조건_명령어}}; then {{echo "Condition is true"}}; fi`

- 조건 명령어의 종료 상태가 0이면 첫 번째 지정된 명령을 실행하고, 그렇지 않으면 두 번째 지정된 명령을 실행:

`if {{조건_명령어}}; then {{echo "Condition is true"}}; else {{echo "Condition is false"}}; fi`

- 파일([f]ile)이 존재하는지 확인:

`if [[ -f {{경로/대상/파일}} ]]; then {{echo "Condition is true"}}; fi`

- 디렉토리([d]irectory)가 존재하는지 확인:

`if [[ -d {{경로/대상/디렉터리}} ]]; then {{echo "Condition is true"}}; fi`

- 파일이나 디렉터리가 존재하는지([e]xists) 확인:

`if [[ -e {{경로/대상/파일_또는_디렉터리}} ]]; then {{echo "Condition is true"}}; fi`

- 변수가 정의되었는지 아닌지 검사:

`if [[ -n "${{변수}}" ]]; then {{echo "Condition is true"}}; fi`

- 가능한 모든 조건을 나열 (`test`는 `[`의 별칭; 둘 다 일반적으로 `if`와 함께 사용됨):

`man [`
