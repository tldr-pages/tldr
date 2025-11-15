# pest

> 단순성에 중점을 둔 PHP 테스트 프레임워크.
> 더 많은 정보: <https://pestphp.com/docs/cli-api-reference>.

- 현재 디렉토리에 표준 Pest 구성 초기화:

`pest --init`

- 현재 디렉토리의 테스트 실행:

`pest`

- 주어진 그룹으로 주석이 달린 테스트 실행:

`pest --group {{이름}}`

- 테스트를 실행하고 커버리지 보고서를 `stdout`에 출력:

`pest --coverage`

- 커버리지를 포함한 테스트를 실행하고, 커버리지가 최소 퍼센트보다 적으면 실패:

`pest --coverage --min={{80}}`

- 테스트를 병렬로 실행:

`pest --parallel`

- 변이를 포함한 테스트 실행:

`pest --mutate`
