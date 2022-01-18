# xcodebuild

> Build Xcode projects.
> There are no options to get help or version.
> More information: <https://www.manpagez.com/man/1/xcodebuild/>.

- Build workspace:

`xcodebuild -workspace {{workspace_name.workspace}} -scheme {{scheme_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Build project:

`xcodebuild -target {{target_name}} -configuration {{configuration_name}} clean build SYMROOT={{SYMROOT_path}}`

- Show SDKs:

`xcodebuild -showsdks`
