# salt

> 원격 salt 미니언에서 명령을 실행하고 상태를 확인.
> 더 많은 정보: <https://docs.saltproject.io/en/latest/ref/cli/index.html>.

- 연결된 미니언 나열:

`salt '*' test.ping`

- 모든 연결된 미니언에서 highstate 실행:

`salt '*' state.highstate`

- 일부 미니언에서 OS 패키지 관리자(apt, yum, brew)를 사용하여 패키지 업그레이드:

`salt '*.example.com' pkg.upgrade`

- 특정 미니언에서 임의의 명령 실행:

`salt '{{미니언_ID}}' cmd.run "ls "`
