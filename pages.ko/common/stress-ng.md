# stress-ng

> 다양한 방식으로 Linux 시스템에 부하를 가하고 스트레스 테스트 수행 (CPU, memory, I/O 등).
> 벤치마킹, 하드웨어 검증 및 안정성 테스트에 유용.
> 더 많은 정보: <https://manned.org/stress-ng>.

- 4개의 워커로 모든 CPU에 60초 동안 부하 적용:

`stress-ng {{[-c|--cpu]}} 4 {{[-t|--timeout]}} 60s`

- 2개의 워커와 512MB 메모리로 가상 메모리에 30초 동안 부하 적용:

`stress-ng {{[-m|--vm]}} 2 --vm-bytes {{512M}} {{[-t|--timeout]}} 30s`

- 3개의 워커로 I/O 서브시스템에 45초 동안 부하 적용:

`stress-ng {{[-i|--io]}} 3 {{[-t|--timeout]}} 45s`

- 모든 스트레스 테스트를 2분 동안 실행:

`stress-ng {{[-a|--all]}} {{1}} {{[-t|--timeout]}} 2m`
