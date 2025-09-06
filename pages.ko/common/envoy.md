# envoy

> Laravel 원격 서버를 위한 PHP 기반 작업 관리자.
> 더 많은 정보: <https://laravel.com/docs/envoy>.

- 구성 파일을 초기화:

`envoy init {{호스트_파일}}`

- 작업 실행:

`envoy run {{작업_이름}}`

- 특정 프로젝트에서 작업 실행:

`envoy run --path {{경로/대상/디렉터리}} {{작업_이름}}`

- 작업을 실행하고 실패 시 계속 진행:

`envoy run --continue {{작업_이름}}`

- 검사를 위해 작업을 Bash 스크립트로 덤프:

`envoy run --pretend {{작업_이름}}`

- SSH를 통해 지정된 서버에 연결:

`envoy ssh {{서버_이름}}`
