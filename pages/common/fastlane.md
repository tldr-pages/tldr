# fastlane

> Build and release mobile applications from the command-line.
> More information: <https://docs.fastlane.tools/actions/>.

- Build and sign the iOS application in the local path:

`fastlane run build_app`

- Run `pod install` for the project in the local path:

`fastlane run cocoapods`

- Delete the derived data from Xcode:

`fastlane run clear_derived_data`

- Remove the cache for pods:

`fastlane run clean_cocoapods_cache`
