# pio remote

> PlatformIO 원격 개발을 위한 보조 명령어.
> `pio remote [command]`는 로컬에서 실행되는 `pio [command]`와 동일한 인수를 사용합니다.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/remote/index.html>.

- 활성화된 모든 원격 에이전트 나열:

`pio remote agent list`

- 특정 이름으로 새로운 원격 에이전트를 시작하고 친구들과 공유:

`pio remote agent start --name {{에이전트_이름}} --share {{example1@example.com}} --share {{example2@example.com}}`

- 지정된 에이전트의 장치 나열 (`--agent`를 생략하여 모든 에이전트 지정 가능):

`pio remote --agent {{에이전트_이름1}} --agent {{에이전트_이름2}} device list`

- 원격 장치의 직렬 포트에 연결:

`pio remote --agent {{에이전트_이름}} device monitor`

- 지정된 에이전트에서 모든 타겟 실행:

`pio remote --agent {{에이전트_이름}} run`

- 특정 에이전트에서 설치된 코어 패키지, 개발 플랫폼 및 전역 라이브러리 업데이트:

`pio remote --agent {{에이전트_이름}} update`

- 특정 에이전트에서 모든 환경의 모든 테스트 실행:

`pio remote --agent {{에이전트_이름}} test`
