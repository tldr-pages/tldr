# bats

> Bash 자동 테스트 시스템: Bash용 TAP (<https://testanything.org/>) 호환 테스트 프레임워크.
> 더 많은 정보: <https://bats-core.readthedocs.io/en/stable/usage.html>.

- BATS 테스트 스크립트를 실행하고 결과를 [t]AP (Test Anything Protocol) 형식으로 출력:

`bats --tap {{경로/대상/test.bats}}`

- 테스트를 실행하지 않고 테스트 스크립트의 테스트 케이스 수([c]ount)를 계산:

`bats --count {{경로/대상/test.bats}}`

- BATS 테스트 케이스를 반복적으로([r]ecursively) 실행 (`.bats` 확장자를 가진 파일):

`bats --recursive {{경로/대상/디렉터리}}`

- 특정 형식([F]ormat)으로 결과를 출력:

`bats --formatter {{pretty|tap|tap13|junit}} {{경로/대상/test.bats}}`

- 테스트에 타이밍([T]iming) 정보 추가:

`bats --timing {{경로/대상/test.bats}}`

- 특정 개수의 작업([j]obs)을 병렬로 실행 (GNU `parallel` 을 설치해야 함):

`bats --jobs {{number}} {{경로/대상/test.bats}}`
