# apt-file

> `apt` 패키지에서 아직 설치되지 않은 파일 검색.
> 더 많은 정보: <https://manned.org/apt-file.1>.

- 메타데이터 데이터베이스 업데이트:

`sudo apt update`

- 지정된 파일 또는 경로를 포함하는 패키지 검색:

`apt-file {{search|find}} {{부분_경로/대상/파일}}`

- 특정 패키지의 내용 나열:

`apt-file {{show|list}} {{패키지}}`

- `정규_표현식`과 일치하는 패키지 검색:

`apt-file {{search|find}} {{[-x|--regexp]}} {{정규_표현식}}`
