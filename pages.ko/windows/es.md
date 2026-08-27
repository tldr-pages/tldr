# es

> Windows용 빠른 파일 및 폴더 검색 도구인 Everything의 명령줄 인터페이스.
> Everything이 설치되어 있으며 백그라운드에서 실행 중이어야 함.
> 더 많은 정보: <https://www.voidtools.com/support/everything/command_line_interface/>.

- 이름으로 파일 또는 폴더 검색:

`es {{검색_문자열}}`

- 정규식(`regex`)을 사용하여 검색:

`es -r {{정규식}}`

- 단어 전체가 일치하는 항목 검색:

`es -w {{검색_문자열}}`

- 표시할 검색 결과 수 제한:

`es -n {{10}} {{검색_문자열}}`

- 지정한 폴더에서 검색:

`es -path {{폴더_경로}} {{검색_문자열}}`

- 폴더만 표시:

`es /ad`

- 파일만 표시:

`es /a-d`

- 결과 정렬 (예: 이름 오름차순):

`es -sort {{name-ascending}}`
