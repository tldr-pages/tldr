# cbt

> Google Cloud's Bigtable에서 데이터를 읽는 유틸리티.
> 더 많은 정보: <https://cloud.google.com/bigtable/docs/cbt-reference>.

- 현재 프로젝트의 테이블 나열:

`cbt ls`

- 현재 프로젝트의 특정 테이블에 있는 행 수를 인쇄:

`cbt count "{{테이블_이름}}"`

- 현재 프로젝트의 열 당 1개의 (가장 최근) 셀 수정만 사용하여 특정 테이블의 단일 행을 표시:

`cbt lookup "{{테이블_이름}}" "{{열_키}}" cells-per-column={{1}}`

- 현재 프로젝트에서 특정 열만 있는 단일 행 표시 (전체 패밀리를 반환하려면 한정자를 생략):

`cbt lookup "{{테이블_이름}}" "{{열_키}}" columns="{{family1:qualifier1,family2:qualifier2,...}}"`

- 특정 정규식 패턴으로 현재 프로젝트에서 최대 5개 행을 검색하고 인쇄:

`cbt read "{{테이블_이름}}" regex="{{열_키_패턴}}" count={{5}}`

- 특정 행 범위를 읽고, 현재 프로젝트에서 반환된 행 키만 인쇄:

`cbt read {{테이블_이름}} start={{시작_열_키}} end={{마지막_열_키}} keys-only=true`
