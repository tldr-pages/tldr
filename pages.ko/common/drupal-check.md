# drupal-check

> 더 이상 사용되지 않는 Drupal PHP 코드를 확인.
> 더 많은 정보: <https://github.com/mglaman/drupal-check#usage>.

- 더 이상 사용되지 않는 특정 디렉터리의 코드를 확인:

`drupal-check {{경로/대상/디렉터리}}`

- 쉼표로 구분된 디렉터리 목록을 제외한 코드를 확인:

`drupal-check --exclude-dir {{경로/대상/제외된_디렉터리}},{{경로/대상/제외된_파일/*.php}} {{경로/대상/디렉터리}}`

- 진행률 표시줄을 표시하지 않음:

`drupal-check --no-progress {{경로/대상/디렉터리}}`

- 잘못된 코딩 관행을 탐지하기 위해 정적 분석을 수행:

`drupal-check --analysis {{경로/대상/디렉터리}}`
