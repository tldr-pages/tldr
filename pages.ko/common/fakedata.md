# fakedata

> 다양한 생성기를 사용하여 가짜 데이터를 생성.
> 더 많은 정보: <https://github.com/lucapette/fakedata>.

- 유효한 모든 생성기를 나열:

`fakedata --generators`

- 하나 이상의 생성기를 사용하여 데이터를 생성:

`fakedata {{생성기1}} {{생성기2}}`

- 특정 출력 형식으로 데이터를 생성:

`fakedata --format {{csv|tab|sql}} {{생성기}}`

- 주어진 수의 데이터 항목을 생성 (기본값은 10):

`fakedata --limit {{n}} {{생성기}}`

- 사용자 정의 출력 템플릿을 사용하여 데이터를 생성 (생성기 이름의 첫 글자는 대문자여야 함):

`echo "{{\{\{Generator\}\}}}" | fakedata`
