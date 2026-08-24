# pio run

> PlatformIO 프로젝트 타겟 실행.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_run.html>.

- 사용 가능한 모든 프로젝트 타겟 나열:

`pio run --list-targets`

- 특정 환경의 사용 가능한 모든 프로젝트 타겟 나열:

`pio run --list-targets {{[-e|--environment]}} {{환경}}`

- 모든 타겟 실행:

`pio run`

- 지정된 환경의 모든 타겟 실행:

`pio run {{[-e|--environment]}} {{환경1}} {{[-e|--environment]}} {{환경2}}`

- 특정 타겟 실행:

`pio run {{[-t|--target]}} {{타겟1}} {{[-t|--target]}} {{타겟2}}`

- 지정된 설정 파일의 타겟 실행:

`pio run {{[-c|--project-conf]}} {{경로/대상/platformio.ini}}`
