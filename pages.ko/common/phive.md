# phive

> 안전한 PHP 애플리케이션 배포를 위한 Phar 설치 및 검증 환경.
> 더 많은 정보: <https://phar.io/#Usage>.

- 사용 가능한 별칭이 있는 Phar 목록 표시:

`phive list`

- 지정한 Phar를 로컬 디렉터리에 설치:

`phive install {{별칭|url}}`

- 지정한 Phar를 전역적으로 설치:

`phive install {{별칭|url}} --global`

- 지정한 Phar를 대상 디렉터리에 설치:

`phive install {{별칭|url}} --target {{경로/대상/폴더}}`

- 모든 Phar 파일을 최신 버전으로 업데이트:

`phive update`

- 지정한 Phar 파일 제거:

`phive remove {{별칭|url}}`

- 사용하지 않는 Phar 파일 제거:

`phive purge`

- 사용 가능한 모든 명령 나열:

`phive help`
