# salt-call

> 로컬에서 salt minion에서 salt를 호출합니다.
> 더 많은 정보: <https://docs.saltproject.io/en/latest/ref/cli/salt-call.html>.

- 이 minion에서 highstate 실행:

`salt-call state.highstate`

- highstate 시뮬레이션 실행, 모든 변경 사항을 계산하지만 실제로 수행하지 않음:

`salt-call state.highstate test=true`

- 자세한 디버깅 출력과 함께 highstate 실행:

`salt-call -l debug state.highstate`

- 이 minion의 grains 나열:

`salt-call grains.items`
