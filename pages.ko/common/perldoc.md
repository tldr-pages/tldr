# perldoc

> `.pod` 형식의 Perl 문서를 조회.
> 더 많은 정보: <https://perldoc.perl.org/perldoc>.

- 내장 함수, 변수 또는 API에 대한 문서 보기:

`perldoc -{{f|v|a}} {{이름}}`

- Perl FAQ의 질문 제목에서 검색:

`perldoc -q {{정규식}}`

- 출력을 직접 `stdout`으로 전송 (기본적으로 페이저로 전송됨):

`perldoc -T {{페이지|모듈|프로그램|URL}}`

- 원하는 번역의 언어 코드를 지정:

`perldoc -L {{언어_코드}} {{페이지|모듈|프로그램|URL}}`
