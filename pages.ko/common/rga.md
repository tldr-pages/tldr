# rga

> 다양한 파일 유형 검색 기능을 가진 Ripgrep 래퍼.
> 더 많은 정보: <https://github.com/phiresky/ripgrep-all>.

- 현재 디렉토리의 모든 파일에서 패턴을 재귀적으로 검색:

`rga {{정규_표현식}}`

- 사용 가능한 어댑터 나열:

`rga --rga-list-adapters`

- 사용할 어댑터 변경 (예: ffmpeg, pandoc, poppler 등):

`rga --rga-adapters={{어댑터1,어댑터2}} {{정규_표현식}}`

- 파일 확장자 대신 MIME 유형을 사용하여 패턴 검색 (느림):

`rga --rga-accurate {{정규_표현식}}`

- 도움말 표시:

`rga --help`
