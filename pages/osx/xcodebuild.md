# xcodebuild

> Build Xcode projects.
> More information: <https://developer.apple.com/library/archive/technotes/tn2339/_index.html>.

- Build workspace:

`xcodebuild -workspace {{workspace_name.workspace}} -scheme {{scheme_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Build project:

`xcodebuild -target {{target_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Show SDKs:

`xcodebuild -showsdks`
