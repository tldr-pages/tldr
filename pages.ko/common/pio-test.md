# pio test

> PlatformIO 프로젝트에서 로컬 테스트 실행.
> 더 많은 정보: <https://docs.platformio.org/en/latest/core/userguide/cmd_test.html>.

- 현재 PlatformIO 프로젝트의 모든 환경에서 모든 테스트 실행:

`pio test`

- 특정 환경에서만 테스트 실행:

`pio test --environment {{환경1}} --environment {{환경2}}`

- 이름이 특정 글로브 패턴과 일치하는 테스트만 실행:

`pio test --filter "{{패턴}}"`

- 이름이 특정 글로브 패턴과 일치하는 테스트를 무시:

`pio test --ignore "{{패턴}}"`

- 펌웨어 업로드를 위한 포트 지정:

`pio test --upload-port {{업로드_포트}}`

- 테스트 실행을 위한 사용자 정의 설정 파일 지정:

`pio test --project-conf {{경로/대상/platformio.ini}}`
