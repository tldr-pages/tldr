# phpstan

> 코드의 버그를 발견하기 위한 PHP 정적 분석 도구.
> 더 많은 정보: <https://phpstan.org/user-guide/command-line-usage>.

- 하나 이상의 디렉터리 분석:

`phpstan analyse {{경로/대상/디렉터리1 경로/대상/디렉터리2 ...}}`

- 구성 파일을 사용하여 디렉터리 분석:

`phpstan analyse {{경로/대상/디렉터리}} --configuration {{경로/대상/구성}}`

- 특정 규칙 레벨을 사용하여 분석 (0-7, 숫자가 높을수록 엄격함):

`phpstan analyse {{경로/대상/디렉터리}} --level {{레벨}}`

- 분석 전에 로드할 자동 로드 파일 지정:

`phpstan analyse {{경로/대상/디렉터리}} --autoload-file {{경로/대상/자동로드_파일}}`

- 분석 중 메모리 제한 지정:

`phpstan analyse {{경로/대상/디렉터리}} --memory-limit {{메모리_제한}}`

- 분석을 위한 사용 가능한 옵션 표시:

`phpstan analyse --help`
