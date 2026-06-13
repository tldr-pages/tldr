# xcodebuild

> Xcode 프로젝트 빌드.
> 더 많은 정보: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- 워크스페이스 빌드:

`xcodebuild -workspace {{워크스페이스_이름.workspace}} -scheme {{스킴_이름}} -configuration {{구성_이름}} clean build SYMROOT={{SYMROOT_경로}}`

- 프로젝트 빌드:

`xcodebuild -target {{대상_이름}} -configuration {{구성_이름}} clean build SYMROOT={{SYMROOT_경로}}`

- SDK 표시:

`xcodebuild -showsdks`
