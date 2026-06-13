# select

> 메뉴를 생성하기 위한 Bash 내장 구조.
> 더 많은 정보: <https://www.gnu.org/software/bash/manual/bash.html#index-select>.

- 개별 단어로 메뉴 생성:

`select {{단어}} in {{사과 오렌지 배 바나나}}; do echo ${{단어}}; done`

- 다른 명령의 출력으로 메뉴 생성:

`select {{줄}} in $({{명령}}); do echo ${{줄}}; done`

- `select`의 프롬프트 문자열을 지정하고 현재 디렉토리에서 파일이나 폴더를 선택하는 메뉴 생성:

`PS3="{{파일을 선택하세요: }}"; select {{파일}} in *; do echo ${{파일}}; done`

- Bash 배열로 메뉴 생성:

`{{과일들}}=({{사과 오렌지 배 바나나}}); select {{단어}} in ${{{과일들[@]}}}; do echo ${{단어}}; done`
