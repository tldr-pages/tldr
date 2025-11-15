# fastlane

> 모바일 애플리케이션 구축 및 출시.
> 더 많은 정보: <https://docs.fastlane.tools/actions/>.

- 현재 디렉터리에서 iOS 애플리케이션을 빌드하고 서명:

`fastlane run build_app`

- 현재 디렉터리의 프로젝트에 대해 `pod install`을 실행:

`fastlane run cocoapods`

- Xcode에서 파생된 데이터 삭제:

`fastlane run clear_derived_data`

- pod의 캐시 제거:

`fastlane run clean_cocoapods_cache`
