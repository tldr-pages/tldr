# ecpg

> C 프로그램을 위한 Embedded SQL 전처리기.
> 더 많은 정보: <https://www.postgresql.org/docs/current/app-ecpg.html>.

- 특정 파일 전처리:

`ecpg {{입력파일.pgc}}`

- `stdin`에서 입력받아 `stdout`으로 출력:

`ecpg -o - -`

- `stdin`에서 입력받아 파일로 출력:

`cat input.pgc | ecpg -o output.c -`

- 출력 파일을 지정하여 전처리:

`ecpg -o {{출력파일.c}} {{입력파일.pgc}}`

- 헤더 파일 전처리 (`.pgh` 확장자):

`ecpg {{입력파일.pgh}}`

- 특정 호환 모드로 전처리:

`ecpg -C {{INFORMIX|INFORMIX_SE|ORACLE}} {{입력파일.pgc}}`

- 자동 커밋 활성화하여 전처리:

`ecpg -t {{입력파일.pgc}}`
