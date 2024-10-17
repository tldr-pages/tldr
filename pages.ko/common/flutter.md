# flutter

> Google의 무료 오픈 소스 크로스 플랫폼 모바일 앱 SDK.
> `pub`과 같은 일부 하위 명령에는 자체 사용법 문서가 있음.
> 더 많은 정보: <https://github.com/flutter/flutter/wiki/The-flutter-tool>.

- 동일한 이름의 디렉터리에서 새로운 Flutter 프로젝트를 초기화:

`flutter create {{프로젝트_이름}}`

- 모든 외부 도구가 올바르게 설치되었는지 확인:

`flutter doctor`

- Flutter 채널 나열 또는 변경:

`flutter channel {{stable|beta|dev|master}}`

- 시작된 모든 에뮬레이터와 연결된 장치에서 Flutter를 실행:

`flutter run -d all`

- 프로젝트 루트의 터미널에서 테스트를 실행:

`flutter test {{test/예시_테스트.dart}}`

- 대부분의 최신 스마트폰을 대상으로 하는 출시 APK를 구축:

`flutter build apk --target-platform {{android-arm}},{{android-arm64}}`

- 특정 명령에 대한 도움말을 표시:

`flutter help {{명령어}}`
