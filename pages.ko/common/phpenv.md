# phpenv

> 개발 목적을 위한 PHP 버전 관리자.
> 더 많은 정보: <https://github.com/phpenv/phpenv>.

- PHP 버전을 전역으로 설치:

`phpenv install {{버전}}`

- `phpenv`에 알려진 모든 PHP 바이너리에 대한 shim 파일 새로 고침:

`phpenv rehash`

- 설치된 모든 PHP 버전 나열:

`phpenv versions`

- 현재 활성화된 PHP 버전 표시:

`phpenv version`

- 전역 PHP 버전 설정:

`phpenv global {{버전}}`

- 로컬 PHP 버전 설정 (전역 버전보다 우선):

`phpenv local {{버전}}`

- 로컬 PHP 버전 해제:

`phpenv local --unset`
