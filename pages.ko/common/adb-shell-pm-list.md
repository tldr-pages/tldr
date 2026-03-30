# adb shell pm list

> 패키지 관리자에서 관리하는 사용자, 패키지, 권한, 테스트, 권한 그룹, 기능, 라이브러리 목록을 출력.
> 더 많은 정보: <https://developer.android.com/tools/adb>.

- 설치된 모든 패키지 목록 출력:

`adb shell pm list packages`

- 시스템의 모든 사용자 출력:

`adb shell pm list users`

- 모든 권한 그룹 출력:

`adb shell pm list permission-groups`

- 모든 권한 출력:

`adb shell pm list permissions`

- 모든 테스트 패키지 목록 출력:

`adb shell pm list instrumentation`

- 시스템의 모든 기능 출력:

`adb shell pm list features`

- 현재 기기에서 지원하는 모든 라이브러리 출력:

`adb shell pm list libraries`
