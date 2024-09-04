# adb logcat

> 시스템 메시지의 로그 덤프.
> 더 많은 정보: <https://developer.android.com/tools/logcat>.

- 시스템 로그 표시:

`adb logcat`

- 정규 표현식([e]xpression)과 일치하는 행 표시:

`adb logcat -e {{정규_표현식}}`

- 특정 모드(상세 ([V]erbose), 디버그([D]ebug), 정보([I]nfo), 경고([W]arning), 에러([E]rror), 치명적 오류([F]atal), 무음([S]ilent))에서 태그에 대한 로그를 표시하고 다른 태그를 필터링:

`adb logcat {{태그}}:{{모드}} *:S`

- 다른 태그를 무음으로([S]ilencing), 상세 ([V]erbose) 모드에서 React Native 애플리케이션에 대한 로그를 표시:

`adb logcat ReactNative:V ReactNativeJS:V *:S`

- 우선순위 수준이 경고([W]arning) 이상인 모든 태그에 대한 로그 표시:

`adb logcat *:W`

- 특정 PID에 대한 로그 표시:

`adb logcat --pid {{pid}}`

- 특정 패키지의 프로세스에 대한 로그 표시:

`adb logcat --pid $(adb shell pidof -s {{패키지}})`

- 로그 색상 지정(보통 필터와 함께 사용):

`adb logcat -v color`
