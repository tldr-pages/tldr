# xonsh

> Python 기반의 크로스 플랫폼 및 Unix 지향 셸.
> Xonsh(발음: conch)에서 sh/Python 코드를 작성하고 혼합할 수 있습니다.
> 더 많은 정보: <https://xon.sh/contents.html>.

- 대화형 셸 세션 시작:

`xonsh`

- 단일 명령 실행 후 종료:

`xonsh -c "{{명령어}}"`

- 스크립트 파일에서 명령을 실행하고 종료:

`xonsh {{경로/대상/스크립트_파일.xonsh}}`

- 셸 프로세스를 위한 환경 변수를 정의:

`xonsh -D{{이름1}}={{값1}} -D{{이름2}}={{값2}}`

- 지정된 `.xonsh` 또는 `.json` 설정 파일 로드:

`xonsh --rc {{경로/대상/파일1.xonsh}} {{경로/대상/파일2.json}}`

- `.xonshrc` 설정 파일 로딩 건너뜀:

`xonsh --no-rc`
