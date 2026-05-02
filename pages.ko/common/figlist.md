# figlist

> figlet 폰트와 제어 파일 목록을 출력하는 도구.
> 관련 항목: `figlet`, `showfigfonts`, `chkfont`.
> 더 많은 정보: <https://manned.org/figlist>.

- 기본 폰트 디렉터리의 모든 폰트 목록 출력:

`figlist`

- 사용자 정의 디렉터리에서 폰트 목록 출력:

`figlist -d {{경로/대상/디렉터리}}`

- 키워드로 폰트 검색:

`figlist -d {{경로/대상/디렉터리}} | grep {{keyword}}`

- 지정한 디렉터리의 전체 폰트 개수 출력:

`figlist -d {{경로/대상/디렉터리}} | wc {{[-l|--lines]}}`
