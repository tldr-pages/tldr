# react-native

> React를 사용하여 네이티브 앱을 구축하기 위한 프레임워크.
> 더 많은 정보: <https://github.com/react-native-community/cli/blob/main/docs/commands.md>.

- 동일한 이름의 디렉터리에 새 React Native 프로젝트 초기화:

`react-native init {{프로젝트_이름}}`

- 메트로 번들러 시작:

`react-native start`

- 캐시를 초기화한 상태로 메트로 번들러 시작:

`react-native start --reset-cache`

- 현재 애플리케이션 빌드 및 연결된 Android 기기 또는 에뮬레이터에서 시작:

`react-native run-android`

- 현재 애플리케이션 빌드 및 iOS 시뮬레이터에서 시작:

`react-native run-ios`

- `release` 모드에서 현재 애플리케이션 빌드 및 연결된 Android 기기 또는 에뮬레이터에서 시작:

`react-native run-android --variant={{release}}`

- `logkitty` 시작 및 로그를 `stdout`에 출력:

`react-native log-android`

- iOS 시뮬레이터를 위한 `tail system.log` 시작 및 로그를 `stdout`에 출력:

`react-native log-ios`
