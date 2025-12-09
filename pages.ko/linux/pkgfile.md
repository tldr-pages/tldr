# pkgfile

> Arch 기반 시스템의 공식 저장소에서 패키지의 파일을 검색합니다.
> 같이 보기: `pacman files`, `pacman --files`의 사용법 설명.
> 더 많은 정보: <https://manned.org/pkgfile>.

- pkgfile 데이터베이스 동기화:

`sudo pkgfile --update`

- 특정 파일을 소유한 패키지 검색:

`pkgfile {{파일명}}`

- 패키지가 제공하는 모든 파일 나열:

`pkgfile --list {{패키지}}`

- 패키지가 제공하는 실행 파일 나열:

`pkgfile --list --binaries {{패키지}}`

- 대소문자를 구분하지 않고 특정 파일을 소유한 패키지 검색:

`pkgfile --ignorecase {{파일명}}`

- `bin` 또는 `sbin` 디렉토리에서 특정 파일을 소유한 패키지 검색:

`pkgfile --binaries {{파일명}}`

- 특정 파일을 소유한 패키지를 패키지 버전과 함께 검색:

`pkgfile --verbose {{파일명}}`

- 특정 저장소에서 특정 파일을 소유한 패키지 검색:

`pkgfile --repo {{저장소_이름}} {{파일명}}`
