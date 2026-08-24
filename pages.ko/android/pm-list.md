# pm list

> 안드로이드 패키지 매니저가 관리하는 사용자, 패키지, 권한, 테스트 패키지, 권한 그룹, 기능 및 라이브러리 목록 조회.
> 더 많은 정보: <https://developer.android.com/tools/adb#pm>.

- 설치된 모든 패키지 목록 표시:

`pm list packages`

- 시스템([s]ystem) 애플리케이션 또는 사용자 설치 애플리케이션([3]rd-party)만 표시:

`pm list packages {{-s|-3}}`

- 시스템의 모든 사용자 목록 표시:

`pm list users`

- 알려진 모든 권한 그룹 표시:

`pm list permission-groups`

- 알려진 모든 권한 표시:

`pm list permissions`

- 테스트 패키지 목록 표시:

`pm list instrumentation`

- 기기가 지원하는 기능 목록 표시:

`pm list features`

- 현재 기기가 지원하는 라이브러리 목록 표시:

`pm list libraries`
