# composer

> PHP 프로젝트의 의존성(dependency)을 기반으로 한 매니저 패키지.
> 더 많은 정보: <https://getcomposer.org/doc/03-cli.md>.

- 대화형으로 `composer.json` 파일을 생성:

`composer init`

- 프로젝트의 의존성으로 패키지를 추가하고, `composer.json`에 항목을 추가:

`composer require {{사용자/패키지}}`

- 프로젝트의 `composer.json` 안에 모든 의존성(dependency)를 설치합니다:

`composer install`

- 프로젝트의 패키지를 제거하며 `composer.json` 안의 모든 의존성(dependency)를 제거합니다:

`composer remove {{사용자/패키지}}`

- 프로젝트의 `composer.json` 파일의 모든 의존성(dependency)를 업데이트 합니다:

`composer update`

- `composer.json`을 수동으로 수정한 후 `composer.lock`만 업데이트:

`composer update --lock`

- 특정 의존성 패키지를 설치할 수 없는 이유를 확인:

`composer why-not {{사용자/패키지}}`

- composer를 최신 버전으로 업데이트 합니다:

`composer self-update`
