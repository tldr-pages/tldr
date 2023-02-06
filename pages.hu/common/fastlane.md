# fastlane

> Mobilalkalmazások építése és kiadása a parancssorból. További információ: <https://docs.fastlane.tools/actions/>.

- Az iOS-alkalmazás építése és aláírása az aktuális könyvtárban:

`fastlane run build_app`

- A `pod install` futtatása az aktuális könyvtárban lévő projekthez:

`fastlane run cocoapods`

- Törölje a származtatott adatokat az Xcode-ból:

`fastlane run clear_derived_data`

- Távolítsa el a podok gyorsítótárát:

`fastlane run clean_cocoapods_cache`
