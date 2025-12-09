# apt-cache

> Debian 및 Ubuntu 패키지 검색 도구.
> 더 많은 정보: <https://manned.org/apt-cache.8>.

- 현재 소스에서 패키지 검색:

`apt-cache search {{검색어}}`

- 패키지 정보 표시:

`apt-cache show {{패키지}}`

- 패키지가 설치되어 있고 최신 상태인지 여부 표시:

`apt-cache policy {{패키지}}`

- 패키지의 의존성 표시:

`apt-cache depends {{패키지}}`

- 특정 패키지에 의존하는 패키지 표시:

`apt-cache rdepends {{패키지}}`
