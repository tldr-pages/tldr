# phar

> PHP 아카이브(PHAR)를 생성, 업데이트 또는 추출.
> 더 많은 정보: <https://manned.org/phar>.

- 하나 이상의 파일이나 디렉터리를 Phar 파일에 추가:

`phar add -f {{경로/대상/phar_파일}} {{경로/대상/파일_또는_디렉터리1 경로/대상/파일_또는_디렉터리2 ...}}`

- Phar 파일의 내용 표시:

`phar list -f {{경로/대상/phar_파일}}`

- Phar 파일에서 지정된 파일이나 디렉터리 삭제:

`phar delete -f {{경로/대상/phar_파일}} -e {{파일_또는_디렉터리}}`

- Phar 파일 내 파일과 디렉터리 압축 또는 압축 해제:

`phar compress -f {{경로/대상/phar_파일}} -c {{알고리즘}}`

- Phar 파일에 대한 정보 얻기:

`phar info -f {{경로/대상/phar_파일}}`

- 특정 해시 알고리즘으로 Phar 파일 서명:

`phar sign -f {{경로/대상/phar_파일}} -h {{알고리즘}}`

- OpenSSL 개인 키로 Phar 파일 서명:

`phar sign -f {{경로/대상/phar_파일}} -h openssl -y {{경로/대상/개인_키}}`

- 도움말 및 사용 가능한 해싱/압축 알고리즘 표시:

`phar help`
