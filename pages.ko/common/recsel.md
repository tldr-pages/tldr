# recsel

> recfile에서 레코드를 출력: 사람이 편집할 수 있는 일반 텍스트 데이터베이스.
> 더 많은 정보: <https://www.gnu.org/software/recutils/manual/recutils.html#Invoking-recsel>.

- 이름 및 버전 필드 추출:

`recsel -p name,version {{data.rec}}`

- "~"를 사용하여 주어진 정규 표현식과 문자열 매칭:

`recsel -e "{{필드_이름}} ~ '{{정규_표현식}}' {{data.rec}}"`

- 이름과 버전을 매칭하는 조건 사용:

`recsel -e "name ~ '{{정규_표현식}}' && version ~ '{{정규_표현식}}'" {{data.rec}}`
