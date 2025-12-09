# read

> `stdin`으로부터 데이터를 수신하는 셸 내장 함수.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-read>.

- 키보드로 입력한 데이터를 저장:

`read {{변수}}`

- 입력한 각 줄을 배열의 값으로 저장:

`read -a {{배열}}`

- 읽을 최대 문자 수 지정:

`read -n {{문자_수}} {{변수}}`

- 여러 값을 여러 변수에 할당:

`read {{_ 변수1 _ 변수2}} <<< "{{The surname is Bond}}"`

- 백슬래시(\\)를 이스케이프 문자로 사용하지 않음:

`read -r {{변수}}`

- 입력 전에 프롬프트 표시:

`read -p "{{여기에 입력: }}" {{변수}}`

- 입력한 문자를 표시하지 않음 (비밀 모드):

`read -s {{변수}}`

- `stdin`을 읽고 각 줄에 대해 작업 수행:

`while read line; do {{echo|ls|rm|...}} "$line"; done < {{/dev/stdin|경로/대상/파일|...}}`
