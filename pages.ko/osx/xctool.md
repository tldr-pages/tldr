# xctool

> Xcode 프로젝트 빌드.
> 더 많은 정보: <https://github.com/facebookarchive/xctool#usage>.

- 워크스페이스 없이 단일 프로젝트 빌드:

`xctool -project {{YourProject.xcodeproj}} -scheme {{YourScheme}} build`

- 워크스페이스의 일부인 프로젝트 빌드:

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} build`

- 정리하고, 빌드하고, 모든 테스트 실행:

`xctool -workspace {{YourWorkspace.xcworkspace}} -scheme {{YourScheme}} clean build test`
