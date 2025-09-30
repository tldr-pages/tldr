# xrdb

> 유닉스 계열 시스템을 위한 X 윈도우 서버의 리소스 데이터베이스 도구.
> 더 많은 정보: <https://www.x.org/releases/current/doc/man/man1/xrdb.1.xhtml>.

- 대화형 모드로 `xrdb` 시작:

`xrdb`

- 리소스 파일에서 값(예: 스타일 규칙) 불러오기:

`xrdb -load {{~/.Xresources}}`

- 리소스 데이터베이스를 조회하고 현재 설정된 값 출력:

`xrdb -query`
