# hyperfine

> 커멘드라인 벤치마킹 도구.
> 더 많은 정보: <https://manned.org/hyperfine>.

- 최소 10회 실행하여, 기본 벤치마크를 실행:

`hyperfine '{{make}}'`

- 비교 벤치마크 실행:

`hyperfine '{{make target1}}' '{{make target2}}'`

- 최소 벤치마킹 실행 횟수 변경:

`hyperfine --min-runs {{7}} '{{make}}'`

- 웜업으로 벤치마크 수행:

`hyperfine --warmup {{5}} '{{make}}'`

- 각 벤치마크 실행 전에 명령을 실행 (캐시 지우기, 등):

`hyperfine --prepare '{{make clean}}' '{{make}}'`

- 각 실행마다 단일 매개변수가 변경되는 벤치마크를 실행:

`hyperfine --prepare '{{make clean}}' --parameter-scan {{스레드_수}} {{1}} {{10}} '{{make -j {스레드_수}}}'`
