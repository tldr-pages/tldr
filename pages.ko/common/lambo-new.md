# lambo new

> Laravel과 Valet을 위한 강력한 `laravel new`.
> 더 많은 정보: <https://github.com/tighten/lambo>.

- 새로운 Laravel 애플리케이션 생성:

`lambo new {{앱_이름}}`

- 특정 경로에 애플리케이션 설치:

`lambo new --path={{경로/대상/폴더}} {{앱_이름}}`

- 인증 스캐폴딩 포함:

`lambo new --auth {{앱_이름}}`

- 특정 프론트엔드 포함:

`lambo new --{{vue|bootstrap|react}} {{앱_이름}}`

- 프로젝트 생성 후 `npm` 종속성 설치:

`lambo new --node {{앱_이름}}`

- 프로젝트 생성 후 Valet 사이트 생성:

`lambo new --link {{앱_이름}}`

- 프로젝트와 동일한 이름의 새 MySQL 데이터베이스 생성:

`lambo new --create-db --dbuser={{사용자}} --dbpassword={{비밀번호}} {{앱_이름}}`

- 프로젝트 생성 후 특정 편집기 열기:

`lambo new --editor="{{편집기}}" {{앱_이름}}`
