# infection

> PHP용 코드 변경 테스팅 프레임워크.
> 더 많은 정보: <https://infection.github.io/guide/command-line-options.html>.

- 구성 파일을 사용하여 코드를 분석 (또는 존재하지 않는 경우 새롭게 생성):

`infection`

- 특정 수의 스레드를 사용:

`infection --threads {{스레드_수}}`

- 최소 MSI(Mutation Score Indicator)를 지정:

`infection --min-msi {{백분율}}`

- 최소 적용 코드 MSI를 지정:

`infection --min-covered-msi {{백분율}}`

- 특정 테스트 프레임워크를 사용 (기본값은 PHPUnit):

`infection --test-framework {{phpunit|phpspec}}`

- 테스트에 포함된 코드 줄만 변경:

`infection --only-covered`

- 적용된 코드 변경을 주는 부분을 표시:

`infection --show-mutations`

- 로그 상세 수준을 지정:

`infection --log-verbosity {{default|all|none}}`
