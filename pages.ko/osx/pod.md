# pod

> Swift 및 Objective-C Cocoa 프로젝트를 위한 종속성 관리 도구.
> 더 많은 정보: <https://guides.cocoapods.org/terminal/commands.html>.

- 현재 프로젝트에 기본 내용으로 Podfile 생성:

`pod init`

- Podfile에 정의된 모든 포드를 다운로드 및 설치 (이전에 설치되지 않은 경우):

`pod install`

- 사용 가능한 모든 포드 나열:

`pod list`

- 현재 설치된 포드 중 업데이트가 필요한 포드 표시:

`pod outdated`

- 현재 설치된 모든 포드를 최신 버전으로 업데이트:

`pod update`

- 특정 (이전에 설치된) 포드를 최신 버전으로 업데이트:

`pod update {{포드_이름}}`

- Xcode 프로젝트에서 CocoaPods 제거:

`pod deintegrate {{xcode_프로젝트}}`
