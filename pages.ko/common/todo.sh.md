# todo.sh

> `todo.txt` 파일을 관리하기 위한 간단하고 확장 가능한 셸 스크립트.
> 더 많은 정보: <https://github.com/todotxt/todo.txt-cli>.

- 모든 항목 나열:

`todo.sh ls`

- 프로젝트 및 컨텍스트 태그로 항목 추가:

`todo.sh add '{{설명}} +{{프로젝트}} @{{컨텍스트}}'`

- 항목을 [완료]로 표시:

`todo.sh do {{항목_번호}}`

- 항목 제거:

`todo.sh rm {{항목_번호}}`

- 항목의 [우선순위] 설정 (A-Z):

`todo.sh pri {{항목_번호}} {{우선순위}}`

- 항목 교체:

`todo.sh replace {{항목_번호}} '{{새_설명}}'`
