# progress

> 실행 중인 coreutils의 진행 상태를 표시/모니터링.
> 더 많은 정보: <https://github.com/Xfennec/progress>.

- 실행 중인 coreutils의 진행 상태 표시:

`progress`

- 조용한 모드로 실행 중인 coreutils의 진행 상태 표시:

`progress -q`

- 단일 장기 실행 명령을 시작하고 모니터링:

`{{명령}} & progress --monitor --pid $!`

- 완료까지 남은 시간 추정 포함:

`progress --wait --command {{firefox}}`
