# pio check

> PlatformIO 프로젝트에 대한 정적 분석 검사를 수행.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_check.html>.

- 현재 프로젝트에 대한 기본 분석 검사 수행:

`pio check`

- 특정 프로젝트에 대한 기본 분석 검사 수행:

`pio check --project-dir {{프로젝트_디렉토리}}`

- 특정 환경에 대한 분석 검사 수행:

`pio check --environment {{환경}}`

- 지정된 결함 심각도 유형만 보고하도록 분석 검사 수행:

`pio check --severity {{낮음|중간|높음}}`

- 환경을 처리할 때 상세한 정보 표시와 함께 분석 검사 수행:

`pio check --verbose`
