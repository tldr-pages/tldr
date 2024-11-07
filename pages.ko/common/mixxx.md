# mixxx

> 무료 및 오픈 소스 크로스 플랫폼 DJ 소프트웨어.
> 같이 보기: `lmms`.
> 더 많은 정보: <https://mixxx.org/manual/latest/chapters/appendix.html#command-line-options>.

- Mixxx GUI를 전체 화면으로 시작:

`mixxx --fullScreen`

- 안전한 개발자 모드에서 시작하여 충돌 디버그:

`mixxx --developer --safeMode`

- 오작동 디버그:

`mixxx --debugAssertBreak --developer --loglevel trace`

- 지정된 설정 파일을 사용하여 Mixxx 시작:

`mixxx --resourcePath {{mixxx/res/controllers}} --settingsPath {{경로/대상/설정-파일}}`

- 사용자 정의 컨트롤러 매핑 디버그:

`mixxx --controllerDebug --resourcePath {{경로/대상/매핑-폴더}}`

- 도움말 표시:

`mixxx --help`
