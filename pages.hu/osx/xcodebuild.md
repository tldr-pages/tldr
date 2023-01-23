# xcodebuild

> Xcode projektek építése. További információ: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Munkaterület építése:

`xcodebuild -workspace {{workspace_name.workspace}} -scheme {{scheme_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Projekt építése:

`xcodebuild -target {{target_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- SDK-k megjelenítése:

`xcodebuild -showsdks`
