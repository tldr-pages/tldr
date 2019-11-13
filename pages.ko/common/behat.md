# behat

> Behaviour-Driven 개발을 위한 PHP 프레임워크. 
> 자세한 정보: [https://behat.org](<https://behat.org/>).

- 새로운 Behat 프로젝트 초기화:

`behat --init`

- 모든 테스트 실행:

`behat`

- 지정된 suite에서 모든 테스트 실행:

`behat --suite={{suite_name}}`

- 특정 출력 formatter로 테스트 실행:

`behat --format {{pretty|progress}}`

- 테스트 실행 및 파일로 결과 출력:

`behat --out {{path/to/file}}`

- 테스트 suite에 정의 목록 표시:

`behat --definitions`