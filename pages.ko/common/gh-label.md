# gh label

> GitHub 레이블 작업.
> 더 많은 정보: <https://cli.github.com/manual/gh_label>.

- 현재 디렉토리의 저장소에 대한 레이블 나열:

`gh label list`

- 현재 디렉토리의 저장소에 대한 레이블을 기본 웹 브라우저에서 보기:

`gh label list --web`

- 현재 디렉토리의 저장소에 특정 이름, 설명 및 16진수 형식 색상으로 레이블 생성:

`gh label create {{이름}} --description "{{설명}}" --color {{색상_16진수}}`

- 현재 디렉토리의 저장소에 대한 레이블 삭제 (확인 요청):

`gh label delete {{이름}}`

- 현재 디렉토리의 저장소에 특정 레이블의 이름과 설명 업데이트:

`gh label edit {{이름}} --name {{새_이름}} --description "{{설명}}"`

- 특정 저장소의 레이블을 현재 디렉토리의 저장소로 복제:

`gh label clone {{소유자}}/{{저장소}}`

- 하위 명령에 대한 도움말 표시:

`gh label {{하위_명령}} --help`
