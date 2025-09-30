# pkginfo

> CRUX 시스템에서 패키지 데이터베이스를 조회.
> 더 많은 정보: <https://crux.nu/Main/Handbook3-6#ntoc19>.

- 설치된 패키지 및 버전 나열:

`pkginfo -i`

- 패키지가 소유한 파일 나열:

`pkginfo -l {{패키지}}`

- 패턴과 일치하는 파일의 소유자(들) 나열:

`pkginfo -o {{패턴}}`

- 파일의 풋프린트 출력:

`pkginfo -f {{경로/대상/파일}}`
