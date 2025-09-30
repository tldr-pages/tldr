# pulseaudio

> PulseAudio 사운드 시스템 데몬 및 관리자.
> 더 많은 정보: <https://manned.org/pulseaudio>.

- PulseAudio가 실행 중인지 확인 (0이 아닌 종료 코드는 실행 중이 아님을 의미):

`pulseaudio --check`

- 백그라운드에서 PulseAudio 데몬 시작:

`pulseaudio --start`

- 실행 중인 PulseAudio 데몬 종료:

`pulseaudio {{[-k|--kill]}}`

- 사용 가능한 모듈 나열:

`pulseaudio --dump-modules`

- 현재 실행 중인 데몬에 모듈과 지정된 인수를 로드:

`pulseaudio {{[-L|--load]}} "{{모듈_이름}} {{인수}}"`
