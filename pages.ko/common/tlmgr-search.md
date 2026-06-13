# tlmgr search

> (Perl) 정규 표현식을 사용하여 TeX Live 패키지를 검색.
> 더 많은 정보: <https://www.tug.org/texlive/doc/tlmgr.html#search>.

- 특정 정규 표현식으로 로컬에 설치된 모든 패키지의 이름 및 설명 검색:

`tlmgr search "{{정규_표현식}}"`

- 정규 표현식으로 로컬에 설치된 모든 패키지의 파일 이름 검색:

`tlmgr search --file "{{정규_표현식}}"`

- 정규 표현식으로 로컬에 설치된 모든 패키지의 파일 이름, 패키지 이름 및 설명 검색:

`tlmgr search --all "{{정규_표현식}}"`

- 로컬 설치가 아닌 TeX Live 데이터베이스 검색:

`tlmgr search --global "{{정규_표현식}}"`

- 파일 이름이 아닌 패키지 이름과 설명에 대한 일치 결과를 전체 단어로 제한:

`tlmgr search --all --word "{{정규_표현식}}"`
