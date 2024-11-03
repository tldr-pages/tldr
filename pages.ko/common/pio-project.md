# pio project

> PlatformIO 프로젝트 관리.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/project/>.

- 새 PlatformIO 프로젝트 초기화:

`pio project init`

- 특정 디렉토리에 새 PlatformIO 프로젝트 초기화:

`pio project init --project-dir {{경로/대상/프로젝트_디렉토리}}`

- 보드 ID를 지정하여 새 PlatformIO 프로젝트 초기화:

`pio project init --board {{ATmega328P|uno|...}}`

- 하나 이상의 프로젝트 옵션을 지정하여 새 PlatformIO 기반 프로젝트 초기화:

`pio project init --project-option="{{옵션}}={{값}}" --project-option="{{옵션}}={{값}}"`

- 프로젝트 구성 출력:

`pio project config`
