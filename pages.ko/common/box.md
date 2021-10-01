# box

> Phar의 빌드 및 관리를 위한 PHP 어플리케이션.
> 더 많은 정보: <https://github.com/box-project/box>.

- 새 Phar 파일 작성:

`box build`

- 특정 구성 파일을 사용하여 새 Phar 파일 작성:

`box build -c {{config/의/경로}}`

- PHAR PHP 확장에 대한 정보 표시:

`box info`

- 특정 Phar 파일에 대한 정보 표시:

`box info {{phar_파일/의/경로}}`

- 현재 작업 디렉토리에서 처음으로 발견된 구성 파일 확인:

`box validate`

- 특정 Phar 파일의 서명 확인:

`box verify {{phar_파일/의/경로}}`

- 사용 가능한 모든 명령 및 옵션 표시:

`box help`
