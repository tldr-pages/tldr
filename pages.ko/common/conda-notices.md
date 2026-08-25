# conda notices

> 최신 채널 알림 조회.
> 더 많은 정보: <https://docs.conda.io/projects/conda/en/latest/commands/notices.html>.

- 기본 채널 및 `.condarc`에 설정된 모든 채널의 알림 표시:

`conda notices`

- 특정 채널 포함:

`conda notices {{[-c|--channel]}} {{채널_이름}}`

- 기본 채널 및 `.condarc` 채널을 무시하고 지정한 채널만 사용:

`conda notices {{[-c|--channel]}} {{채널_이름}} --override-channels`
