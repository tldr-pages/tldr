# git hash-object

> 콘텐츠의 고유 해시 키를 계산하고, 선택적으로 지정된 유형의 객체를 생성.
> 더 많은 정보: <https://git-scm.com/docs/git-hash-object>.

- 저장하지 않고 객체 ID 계산:

`git hash-object {{경로/대상/파일}}`

- 객체 ID를 계산하고 Git 데이터베이스에 저장:

`git hash-object -w {{경로/대상/파일}}`

- 객체 유형을 지정하여 객체 ID 계산:

`git hash-object -t {{blob|commit|tag|tree}} {{경로/대상/파일}}`

- `stdin`에서 객체 ID 계산:

`cat {{경로/대상/파일}} | git hash-object --stdin`
