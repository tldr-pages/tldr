# xbps-query

> 패키지 및 저장소 정보를 조회하는 XBPS 유틸리티.
> 같이 보기: `xbps`.
> 더 많은 정보: <https://manned.org/xbps-query.1>.

- 정규 표현식 또는 키워드를 사용하여 원격 저장소에서 패키지 검색 (`--regex`가 생략된 경우 키워드 사용):

`xbps-query --search {{정규_표현식|키워드}} --repository --regex`

- 설치된 패키지에 대한 정보 표시:

`xbps-query --show {{패키지}}`

- 원격 저장소의 패키지 정보 표시:

`xbps-query --show {{패키지}} --repository`

- 패키지 데이터베이스에 등록된 패키지 나열:

`xbps-query --list-pkgs`

- 명시적으로 설치된 패키지 나열 (의존성으로 자동 설치되지 않은 패키지):

`xbps-query --list-manual-pkgs`
