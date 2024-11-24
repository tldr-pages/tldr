# pio ci

> 임의의 소스 코드 구조로 PlatformIO 프로젝트를 빌드.
> 소스 코드가 복사될 새로운 임시 프로젝트를 생성.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_ci.html>.

- 기본 시스템 임시 디렉토리에서 PlatformIO 프로젝트를 빌드하고 이후 삭제:

`pio ci {{경로/대상/프로젝트}}`

- 특정 라이브러리를 지정하여 PlatformIO 프로젝트 빌드:

`pio ci --lib {{경로/대상/라이브러리_폴더}} {{경로/대상/프로젝트}}`

- 특정 보드를 지정하여 PlatformIO 프로젝트 빌드 (`pio boards` 명령어로 모든 보드 목록 확인 가능):

`pio ci --board {{보드}} {{경로/대상/프로젝트}}`

- 특정 디렉토리에서 PlatformIO 프로젝트 빌드:

`pio ci --build-dir {{경로/대상/빌드_디렉토리}} {{경로/대상/프로젝트}}`

- 빌드 디렉토리를 삭제하지 않고 PlatformIO 프로젝트 빌드:

`pio ci --keep-build-dir {{경로/대상/프로젝트}}`

- 특정 구성 파일을 사용하여 PlatformIO 프로젝트 빌드:

`pio ci --project-conf {{경로/대상/platformio.ini}}`
